#!/usr/bin/env python3
"""The Internet in One Word — entry: tirefire.

Writes exactly the word "tirefire" (and nothing else) to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


WORD = "tirefire"


def validate_word(word):
    """Guard: the entry must be exactly one word, 1-30 chars, no spaces."""
    if not isinstance(word, str):
        raise TypeError("entry word must be a string")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry word must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry word must be a single word (no whitespace)")
    if not word.isalpha():
        raise ValueError("entry word must contain letters only")
    return word


def main():
    word = validate_word(WORD)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(OUT_PATH, 0o644)
    # Read-back guard: the file on disk must be exactly the validated word.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != word:
            raise RuntimeError("entry file does not match the validated word")


if __name__ == "__main__":
    main()
