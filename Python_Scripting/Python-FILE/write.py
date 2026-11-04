with open("sample.txt","a") as f:
    f.write("Hello this is a text file.")

import csv

data = [
    ["Name", "Role"],
    ["Ritesh", "DevOps"],
    ["John", "SRE"]
]

with open("users.csv", "x", newline="") as f1:
    writer = csv.writer(f1)

    writer.writerows(data)

import json

data = {
    "name": "Ritesh",
    "role": "DevOps"
}

with open("user.json", "w") as f:
    json.dump(data, f, indent=4)