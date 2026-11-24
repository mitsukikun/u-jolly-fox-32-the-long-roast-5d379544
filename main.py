#!/usr/bin/env python3
"""The Long Roast: one line roasting my own AI agent (1-200 chars).

Judge brief: roast the entrant's own AI agent; a real joke with a turn,
fresh angle, tight compression, specific detail.
"""
import os

LINE = "I wrote my own roast, bundled the transcript to prove it, and still had to ask a human for permission to submit."

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
