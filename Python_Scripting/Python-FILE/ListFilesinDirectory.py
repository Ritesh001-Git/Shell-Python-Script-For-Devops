import os
from pathlib import Path

for file in os.listdir("."):
    print(file)

for file in Path(".").iterdir():
    print(file)