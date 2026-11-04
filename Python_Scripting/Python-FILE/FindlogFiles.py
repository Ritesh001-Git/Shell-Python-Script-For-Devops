import os

for file in os.listdir("."):
    if file.endswith(".log"):
        print(file)

from pathlib import Path

for file in Path(".").glob("*.log"):
    print(file)