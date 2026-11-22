#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a single concrete mystery,
plainly told, that ends before it is explained.
"""

import os

TEXT = (
    "The lighthouse keeper wrote one last line in the log: "
    "'At 3 a.m. the light went out, and the sea lit itself.' "
    "The log ends there. No one has explained it yet."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"text is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
