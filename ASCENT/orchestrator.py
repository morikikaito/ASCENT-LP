"""秘書AI：タスク分解 → 並行dispatch → 統合"""
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import anthropic

from agent import Agent, SHARED_CONTEXT, _load_file, BASE_DIR

# ── エージェント定義 ──
AGENTS = {
    "copywriter": Agent("コピーライターAI", "marketing/RULES.md"),
    "redteam": Agent("レッドチームAI", "redteam/RULES.md"),
    "market": Agent("外部マーケAI", "marketing/external/RULES.md"),
    "sales": Agent("セールスAI", "sales/RULES.md"),
    "product": Agent("プロダクトAI", "product/RULES.md"),
}

# ── 秘書AIのシステムプロンプト ──
SECRETARY_RULES = _load_file(os.path.join(BASE_DIR, "secretary/RULES.md"))
SECRETARY_SYSTEM = SHARED_CONTEXT + "\n\n---\n\n" + SECRETARY_RULES

# ── タスク分解プロンプト ──
DECOMPOSE_SUFFIX = """
あなたは秘書AIです。開斗からの指示を受け取り、どのエージェントに何を依頼するか判断してください。

利用可能なエージェント:
- copywriter: LINE配信文・台本・LP原稿の作成
- redteam: 企画・施策への批判的レビュー
- market: 競合調査・トレンド転用
- sales: クロージング文・アップセル提案
- product: Quick Win設計・チャーン対策・LTV改善

以下のJSON形式で返してください。必ずJSONのみを返し、他のテキストは含めないでください。
必要なエージェントだけを選んでください（全員呼ぶ必要はありません）。

```json
{
  "summary": "開斗の意図を1文で要約",
  "tasks": [
    {"agent": "エージェント名", "instruction": "具体的な指示"}
  ]
}
```
"""

# ── 統合プロンプト ──
INTEGRATE_SUFFIX = """
あなたは秘書AIです。各エージェントの結果を開斗向けにわかりやすく統合してください。

ルール:
- 各エージェントの出力を整理して、すぐ行動できる形にまとめる
- 矛盾があれば指摘する
- 最後に「開斗への提案」として次のアクションを1〜3個提示する
"""


class Orchestrator:
    """秘書AI：会話継続型オーケストレーター"""

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.history = []  # 会話履歴

    def _call_secretary(self, user_message, extra_system=""):
        """秘書AIにメッセージを送る（会話履歴付き）"""
        self.history.append({"role": "user", "content": user_message})

        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            system=SECRETARY_SYSTEM + "\n\n" + extra_system,
            messages=self.history,
            max_tokens=4096,
        )
        assistant_text = response.content[0].text
        self.history.append({"role": "assistant", "content": assistant_text})
        return assistant_text

    def _decompose(self, user_input):
        """開斗の入力をタスクに分解する"""
        raw = self._call_secretary(user_input, DECOMPOSE_SUFFIX)

        # JSONを抽出
        try:
            # ```json ... ``` で囲まれている場合
            if "```json" in raw:
                json_str = raw.split("```json")[1].split("```")[0]
            elif "```" in raw:
                json_str = raw.split("```")[1].split("```")[0]
            else:
                json_str = raw
            return json.loads(json_str.strip())
        except (json.JSONDecodeError, IndexError):
            # パースに失敗したら秘書の回答をそのまま返す
            return None

    def _dispatch(self, tasks):
        """各エージェントに並行でタスクを投げる"""
        results = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {}
            for task in tasks:
                agent_key = task["agent"]
                if agent_key in AGENTS:
                    agent = AGENTS[agent_key]
                    future = executor.submit(
                        agent.run, self.client, task["instruction"]
                    )
                    futures[future] = agent_key

            for future in as_completed(futures):
                agent_key = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    results.append({
                        "agent": agent_key,
                        "result": f"[エラー] {e}"
                    })

        return results

    def _integrate(self, decomposed, results):
        """各エージェントの結果を統合する"""
        report = f"## 開斗の指示\n{decomposed['summary']}\n\n"
        for r in results:
            report += f"## {r['agent']}の回答\n{r['result']}\n\n"

        integrated = self._call_secretary(
            f"以下の各エージェントの結果を統合してください:\n\n{report}",
            INTEGRATE_SUFFIX,
        )
        return integrated

    def _save_log(self, user_input, response):
        """会話ログを保存"""
        log_dir = os.path.join(BASE_DIR, "secretary", "daily_log")
        os.makedirs(log_dir, exist_ok=True)
        today = datetime.now().strftime("%Y-%m-%d")
        log_path = os.path.join(log_dir, f"{today}.md")

        timestamp = datetime.now().strftime("%H:%M")
        entry = f"\n### {timestamp}\n**開斗**: {user_input}\n\n**秘書**: {response[:200]}...\n\n---\n"

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry)

    def process(self, user_input):
        """メイン処理：分解 → 並行実行 → 統合"""
        print("\n🔍 秘書AI：タスクを分解中...")
        decomposed = self._decompose(user_input)

        if decomposed is None:
            # タスク分解不要（壁打ち・雑談等）→ 秘書の直接回答
            response = self.history[-1]["content"]
            self._save_log(user_input, response)
            return response

        tasks = decomposed.get("tasks", [])
        if not tasks:
            response = f"意図: {decomposed.get('summary', '')}\n\n担当エージェントが不要と判断しました。秘書AIが直接対応します。"
            self._save_log(user_input, response)
            return response

        # エージェント表示
        agent_names = [AGENTS[t["agent"]].name for t in tasks if t["agent"] in AGENTS]
        print(f"📋 意図: {decomposed['summary']}")
        print(f"👥 起動: {' / '.join(agent_names)}")
        print("⏳ 各エージェント並行実行中...\n")

        # 並行実行
        results = self._dispatch(tasks)

        # 統合
        print("📊 秘書AI：結果を統合中...\n")
        integrated = self._integrate(decomposed, results)

        self._save_log(user_input, integrated)
        return integrated
