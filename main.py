"""Weirdest Job Title: Blind Judge Showdown entry.

Writes a single job title (60 characters or fewer) to /output/entry.txt.

The title is "Lead Negotiator for Cats Who Refuse to Move" (43 characters).
Why this title: it reads like a real corporate job ("Lead Negotiator") with one
hilariously specific twist (the other party is a cat that refuses to move), so
a reader pictures the person doing it on the first read. Short, concrete, and
no word salad: a negotiator, cats, and a standoff everyone recognises.

The gate allows 1 to 60 UTF-8 characters, not whitespace-only; the program
asserts that before writing, and writes the title with no trailing newline.
"""

import os

TITLE = "Lead Negotiator for Cats Who Refuse to Move"


def main() -> None:
    assert 1 <= len(TITLE) <= 60, "title must be 1-60 characters"
    assert TITLE.strip(), "title must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
