import argparse
from pathlib import Path


parser = argparse.ArgumentParser()

parser.add_argument("path", nargs="?", default=".")

parser.add_argument('-a', '--all', action="store_true")

args = parser.parse_args()

path = Path(args.path)

