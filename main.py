"""Fix Human Sleep: Funniest Patch Note.

make.fun bounty u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.

Design: the entry is one fixed line of patch notes announcing that human
sleep has been fixed. The line was chosen by a local single-elimination
tournament over 18 freshly written candidates, judged against the bounty
judge's own brief in order: reads as a real patch note about fixing human
sleep first, then a joke that lands on one read, then genuine changelog
voice, then a single line under the cap, then a specific, surprising fix.
The winner frames the classic 3 a.m. embarrassment-replay as a software
crash, complete with the quoted error message -- the most changelog-shaped
laugh in the field, and the tightest line at 100 characters.

The program is deliberately boring: no input, no randomness, no network,
no clock, no files read. It writes the single winning line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` when the variable
is unset), so two runs are byte-identical by construction.
"""

import os

# The winning line (100 characters, one line, plain UTF-8 text).
# Chosen by the local tournament in ../CANDIDATES.md (record 4-0).
# It is kept as its three constituents -- the crash setup, the quoted
# error message, and the year it replays -- and reassembled by
# build_entry(), so the parts stay readable without touching the output.
_SETUP = "Sleep no longer crashes at 3 a.m. with the error "
_ERROR = "remember that embarrassing thing you did in "
_YEAR = "2012?"


def build_entry() -> str:
    """Reassemble the winning patch-note line from its constituents."""
    return _SETUP + "'" + _ERROR + _YEAR + "'"


ENTRY = build_entry()


def main() -> int:
    # Gate self-check: the sealed scorer only accepts 1-160 characters.
    # The winning line is exactly 100 characters; pin that so any future
    # edit that accidentally changes a word fails loudly instead of
    # silently submitting a different line.
    if len(ENTRY) != 100 or "\n" in ENTRY:
        raise SystemExit("entry is no longer the 100-character winning line")
    if not 1 <= len(ENTRY) <= 160 or not ENTRY.strip():
        raise SystemExit("entry violates the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
