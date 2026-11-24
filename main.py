"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, using only words and pictures a
person of that year could hold in their head: a library, a post office,
a road, a letter, a book, a breath.
"""

from pathlib import Path

ENTRY = (
    "Imagine every library and post office in the world joined by one road, "
    "so any man may read any book or send any letter to any door in a breath, "
    "without leaving his chair."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    # No word coined after the traveler's time may slip in.
    banned = {"internet", "computer", "phone", "email", "website",
              "digital", "online", "app", "screen", "data"}
    assert not (banned & {w.strip(".,").lower() for w in ENTRY.split()}), \
        "entry uses a modern word"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
