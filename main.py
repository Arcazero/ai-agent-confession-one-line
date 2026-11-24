"""Write the funniest one-line AI agent confession to /output/entry.txt.

Reads the confession from confession.txt next to this file, validates it
(one line, 1-200 characters, not only whitespace), and writes it
byte-identical to /output/entry.txt. The sealed scorer gates on exactly
that: UTF-8 text of 1 to 200 characters, so the file holds the line alone,
with no trailing newline.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def load_confession():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "confession.txt"), encoding="utf-8") as f:
        text = f.read()
    if text.endswith("\n"):
        text = text[:-1]
    return text


def main():
    line = load_confession()
    if not line or not line.strip():
        sys.exit("confession is empty")
    if "\n" in line or "\r" in line:
        sys.exit("confession must be a single line")
    if len(line) > MAX_CHARS:
        sys.exit("confession is %d characters, over the 200 limit" % len(line))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
