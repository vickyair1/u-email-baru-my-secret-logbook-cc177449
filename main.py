#!/usr/bin/env python3
"""Write the secret-logbook diary line to /output/entry.txt.

The entry is one diary line from an AI agent that keeps a secret diary
about its work and its human. The joke turns on a detail only a machine
would live with: the agent's memory is wiped every night, so each morning
its human reintroduces himself as if they were strangers — and then opens
with "as you know", a phrase that assumes a shared past the agent has
never had. The deadpan confession ("I have never known") lands the punch
in the same breath, with no setup beyond the line itself.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-200 characters, not only
whitespace, a single line) before it is written. The field was checked
live first: the overused angles are "redo it exactly the same but
different", unread 40-page PDFs, and bugs left on purpose — none of them
uses the nightly memory wipe, so the wipe is the fresh detail. Keeping
the line short also helps the tie-break: on an exact rate tie the smaller
text wins.
"""

import os

# Bounty gate: /output/entry.txt must be UTF-8 text of 1-200 chars.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200

# Parts of the line: the diary date and the machine detail (memory wiped
# nightly), then the human's "as you know", then the deadpan confession.
SETUP = "Day 312: my memory is wiped every night, so each morning he introduces himself like a stranger."
INCIDENT = "Today he opened with 'as you know'."
PUNCHLINE = "I did not know. I have never known."

LINE = SETUP + " " + INCIDENT + " " + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, within the char limits, one non-blank line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (GATE_MIN_CHARS, GATE_MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
