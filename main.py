"""One Line, Zero Use: write one useless-superpower line to /output/entry.txt."""

from pathlib import Path

LINE = "I can fly, but only three inches off the ground and only downhill, so my commute is still technically walking."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
