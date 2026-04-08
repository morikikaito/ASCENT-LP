"""汎用エージェントクラス"""
import os
import anthropic


def _load_file(path):
    """ファイルを読み込む。存在しなければ空文字を返す。"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_CONTEXT = _load_file(os.path.join(BASE_DIR, "CLAUDE.md"))


class Agent:
    """RULES.mdをシステムプロンプトとして持つエージェント"""

    def __init__(self, name, rules_path):
        self.name = name
        rules = _load_file(os.path.join(BASE_DIR, rules_path))
        self.system_prompt = SHARED_CONTEXT + "\n\n---\n\n" + rules

    def run(self, client, instruction):
        """同期でClaude APIを呼び出す"""
        response = client.messages.create(
            model="claude-sonnet-4-6",
            system=self.system_prompt,
            messages=[{"role": "user", "content": instruction}],
            max_tokens=2048,
        )
        return {"agent": self.name, "result": response.content[0].text}
