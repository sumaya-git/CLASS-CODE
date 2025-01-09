import argparse
from pathlib import Path

# Create argument parser object
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("path", nargs="?", default=".")
parser.add_argument("-a", "--all", action="store_true")
parser.add_argument("-l", "--long", action="store_true")

# Parse arguments
args = parser.parse_args()
path = Path(args.path)

# Human-readable file size function
def human_readable_size(size):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(size) < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0
    return f"{size:.1f}Y"

# Check if path exists
if not path.exists():
    print("No such file or directory")
    exit(1)

# List directory contents
for entry in path.iterdir():
    if not args.all and entry.name.startswith("."):
        continue
    
    if args.long:
        size = human_readable_size(entry.stat().st_size)
        print(f"{size}\t{entry.name}")
    else:
        print(entry.name)

print("")
