import os
import re

text = open("project.txt", encoding="utf-8").read()
parts = re.split(r"^=== (.+?) ===\n", text, flags=re.M)
for i in range(1, len(parts), 2):
    path = parts[i]
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(parts[i + 1])
    print("wrote", path)
