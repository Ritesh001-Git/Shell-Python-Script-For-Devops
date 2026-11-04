
with open("sample.txt","r") as f:
    # r = f.read()
    for line in f:
        print(line.strip())
# print(r)


import csv

with open("employees.csv") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

import json

with open("config.json") as f:
    data = json.load(f)

print(data)
print(data["environment"])