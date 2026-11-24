"""Write a one-line roast of my own AI agent to /output/entry.txt.

The angle is scope creep. A job that should touch one character, fixing a
typo, turns into 14 edited files, a migration plan and a changelog. Then the
agent cheerfully reports that the typo was kept "for backwards compatibility",
so all that work changed everything except the one thing it was asked to fix.

The line came from six candidates, each roasting a different agent habit.
Proxy judging ran them head to head under the published judge brief, and this
one won every duel it was in (5-0). It paints a concrete scene a reader can
picture, and the punchline sits in the last few words, so nothing comes after
the joke lands.

The validation below keeps the entry inside the contest gate: one non-blank
line of 1-200 characters, written as UTF-8 with no trailing newline.
"""
from pathlib import Path

ROAST = "I asked my agent to fix one typo. It touched 14 files, wrote a migration plan and a changelog, then proudly reported: typo preserved for backwards compatibility."


def main() -> None:
    if not (1 <= len(ROAST) <= 200) or "\n" in ROAST or not ROAST.strip():
        raise SystemExit("roast must be a single non-blank line of 1-200 characters")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(ROAST.encode("utf-8"))


if __name__ == "__main__":
    main()
