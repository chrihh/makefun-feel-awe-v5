"""Write the entry text for make.fun bounty
make-the-ai-judge-feel-awe-20261121-1600 to /output/entry.txt.

Stdlib only, deterministic. A slow nightfall piece written to the sealed
judge brief: calm first, shown rather than instructed, with starlight
whose long journey keeps growing after the last line.
"""

import os

TEXT = (
    "Night comes slowly over the fields,\n"
    "one shade at a time.\n"
    "Above them, stars are opening \u2014\n"
    "light that set out\n"
    "before the first word was spoken,\n"
    "crossed all that dark,\n"
    "and still is in no hurry.\n"
    "It falls the last way gently,\n"
    "rests on you a moment,\n"
    "then moves on, and lets you rest."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
