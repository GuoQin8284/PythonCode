import yaml
data = open("./type_data.yaml", mode="r", encoding="utf-8")
load_data = yaml.safe_load(data)
print(load_data)
for i in load_data.values():
    print(type(i))

data.close()