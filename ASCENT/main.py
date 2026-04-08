#!/usr/bin/env python3
"""ASCENT AI社員チーム — CLI"""
import sys

from orchestrator import Orchestrator


def main():
    print("=" * 50)
    print("  ASCENT AI社員チーム")
    print("  No Limits — 非日常を当たり前に")
    print("=" * 50)
    print()
    print("開斗、何でも言ってください。")
    print("（終了: quit / 履歴リセット: reset）")
    print()

    orch = Orchestrator()

    # コマンドライン引数があればワンショット実行
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        print(f"開斗> {user_input}\n")
        response = orch.process(user_input)
        print(response)
        return

    # 対話モード
    while True:
        try:
            user_input = input("開斗> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nお疲れ様でした。")
            break

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("お疲れ様でした。")
            break
        if user_input.lower() == "reset":
            orch = Orchestrator()
            print("会話履歴をリセットしました。\n")
            continue

        response = orch.process(user_input)
        print()
        print(response)
        print()


if __name__ == "__main__":
    main()
