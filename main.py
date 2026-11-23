#!/usr/bin/env python3
"""Six Words, One Story.

A complete story in exactly six words, on any subject:

    He counted stars. One counted back.

A stargazer counts the stars; then one of them counts back.
The turn is in the second sentence, and who — or what — is
counting back is left for the reader to fill in. Every word
earns its place: the first sentence sets the scene, the second
flips it.

The program writes the story to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set) and prints it.
It is deterministic, uses no network, and writes the same text
on every run. Before writing, it checks the story against the
bounty's gate: exactly six words and 1 to 60 characters.
"""

import os
import sys

STORY = "He counted stars. One counted back."


def word_count(text: str) -> int:
    """Words are separated by whitespace."""
    return len(text.split())


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    words = word_count(STORY)
    if words != 6:
        print(
            f"error: story must be exactly six words, got {words}",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(STORY) <= 60 or not STORY.strip():
        print("error: story must be 1 to 60 non-blank characters", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
