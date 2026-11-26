#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun micro entry.

Writes a single word describing my Wi-Fi to /output/entry.txt.
Standard library only, no network, no randomness: the output is
byte-identical on every run.
"""

WORD = "Schrödinger"
# Why this word: my Wi-Fi is simultaneously connected and not connected --
# full bars until the moment something actually needs it, at which point
# it collapses into nothing. You only find out which state it was in by
# trying to load a page, exactly like opening the box.


def main() -> None:
    assert WORD, "entry word must not be empty"
    assert WORD == WORD.strip(), "entry word must have no surrounding whitespace"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(WORD) <= 32, "entry word length out of range"

    data = WORD.encode("utf-8")
    with open("/output/entry.txt", "wb") as fh:
        fh.write(data)

    with open("/output/entry.txt", "rb") as fh:
        written = fh.read()
    assert written == data, "written bytes do not match entry word"
    assert b"\n" not in written, "entry must be a single line with no newline"


if __name__ == "__main__":
    main()
