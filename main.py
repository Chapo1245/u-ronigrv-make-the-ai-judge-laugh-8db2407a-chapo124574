#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line (1-200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

ENTRY = (
    "My performance review is written by an AI, graded by an AI, "
    "and appealed to my human \u2014 who asked me to write the appeal."
)


def main() -> None:
    # The gate allows 1-200 characters of UTF-8 text, one line.
    # ENTRY is 120 characters, so it passes with room to spare.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
