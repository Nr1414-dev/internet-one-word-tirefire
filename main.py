#!/usr/bin/env python3
"""The Internet in One Word — entry: tirefire.

Writes exactly the word "tirefire" (and nothing else) to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("tirefire")
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
