#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes a single original English sentence, phrased as an absurd clause
that could sit buried deep inside a terms-of-service agreement, to
/output/entry.txt. The clause is deterministic: the same line every run.
"""

import os

ENTRY = (
    "By accepting these Terms, you grant us a perpetual licence to your "
    "firstborn child's first word, which shall henceforth be the word "
    "'synergy'."
)

# The gate requires /output/entry.txt to hold UTF-8 text of 1 to 200
# characters, not only white space. One sentence, no setup, no punchline
# explained: the legal register carries the joke until "synergy" lands.
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry stripped, or raise if it fails the gate."""
    entry = text.strip()
    if not entry:
        raise ValueError("entry is empty")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over {MAX_CHARS}")
    if entry.count(".") != 1 or not entry.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return entry


def main() -> None:
    text = validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)
    print(f"characters: {len(text)}")


if __name__ == "__main__":
    main()
