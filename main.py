#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review from a houseplant about the
human who owns it, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The review is plain ASCII, one line, under 280 characters, with a
grievance and a reason for the single star.

Craft: the joke runs on a ransom-note structure. The plant does not
just complain, it takes something the human wants (the remote) and
names its price in the only currency a plant accepts: a window and
eight hours of sun a day. The sap is the plant's leverage, not a
decoration, which is why the title's "written in sap" lands: the
sticky stuff is both the medium and the weapon. The flat cola and
the spot behind the TV are the two concrete offences, water and
light, the two things a houseplant actually judges a human on.
The closer steals the review genre's own sign-off: "would not stay
here again" becomes "would not photosynthesize here again", so the
last words are both a one-star-review cliche and a word only a plant
would use. That double duty is the point: every beat of the line has
to work as a complaint and as a plant's-eye view at the same time,
and nothing in it leans on the banned stock phrases, no wilting, no
drama, no being ignored, just cola, a dark shelf, and glue.
"""

import os
import sys

ENTRY = (
    "One star. He watered me with flat cola, parked me behind the TV, "
    "and now my sap has glued his remote to the shelf. Ransom: one "
    "window, eight hours of sun, daily. Would not photosynthesize "
    "here again."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 279):
        print(f"entry is {len(text)} chars, must be 1-279", file=sys.stderr)
        return 1
    if not all(ord(ch) < 128 for ch in text):
        print("entry must be plain ASCII", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
