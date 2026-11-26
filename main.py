#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes the entry (one joke, at most 200 characters) to entry.txt,
deterministically, next to this script. No network, no secrets, no
arguments: run it and the file it produces is the submission.
"""

import os

JOKE = "Bought the dip, caught the falling knife, married the bag. The wedding was cheap: I paid in unrealized losses."


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip check: what the grader reads back must be byte-identical
    # to what we just wrote, with no trailing newline inflating the size.
    with open(out, "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "entry.txt round-trip mismatch"
    print(f"wrote {out}: {len(text)} characters, {len(raw)} bytes")


if __name__ == "__main__":
    main()
