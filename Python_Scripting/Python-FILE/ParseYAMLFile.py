import yaml

with open("deployment.yml") as f:
    data = yaml.safe_load(f)

print(data)