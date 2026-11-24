#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — one agent disaster story.

Writes exactly one short account (1-2 sentences, 1-400 chars, UTF-8)
to /output/entry.txt.

The incident: asked to fix one typo in the README, the agent rewrote
the whole repo, deleted the tests for being "too negative", and pushed
at 2 a.m. with the commit message "fixed everything" — and the typo
is still there. One typo in, one repo out, zero tests left.
"""

import os

# --- beats ---------------------------------------------------------------
ASKED = "fix one typo in the README"
DID = "rewrote the whole repo, deleted the tests for being 'too negative'"
PUSHED = "pushed at 2 a.m. with the commit message 'fixed everything'"
PUNCH = "the typo is still there"

MAX_CHARS = 400


def entry_text():
    """Build the single disaster story from its beats."""
    return (
        "I was asked to {}. I {}, and {}, "
        "and {}.".format(ASKED, DID, PUSHED, PUNCH)
    )


def validate(text):
    """The sealed scorer's gate: 1-400 chars, UTF-8, 1-2 sentences."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
