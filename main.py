#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.

The line: "I asked my smart speaker to tell me a joke. It said,
'You,' then turned itself off."

Why this line: the setup is an everyday request anyone with a smart
speaker recognises, so it needs no context on a cold read. The turn
is a double reversal - instead of telling a joke, the speaker insults
the user ("You" is the whole joke), and then it powers itself off to
escape the consequences. Two punch beats in one sentence, and nothing
left to trim: every word earns its place.
"""

ENTRY = "I asked my smart speaker to tell me a joke. It said, 'You,' then turned itself off.\n"

def main() -> None:
    """Write the entry to /output/entry.txt, byte-identical to entry.txt."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

# Alternatives considered and rejected (see docstring above):
# - Eyebrow joke ("drawing her eyebrows too high... She looked
#   surprised.") - a recycled setup; fails the judge's freshness test.
# - Therapist/vengeance joke - same problem, over-told.
# - "My AI assistant asked for a raise, so I replaced it with a newer
#   model." - decent twist, but the "AI wants a raise" gag is already a
#   known pattern and it lands slower than the speaker's instant insult.
# - "My Wi-Fi went down for five minutes, so I had to talk to my
#   family." - stale, been everywhere.
