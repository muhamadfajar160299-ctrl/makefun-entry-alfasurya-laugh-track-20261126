import os
# Output dir is taken from the environment so the entry lands where the grader expects.
import sys

LINE = "Bought the dip, caught the falling knife, married the bag. The wedding was cheap: I paid in unrealized losses."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0

if __name__ == "__main__":
    sys.exit(main())
