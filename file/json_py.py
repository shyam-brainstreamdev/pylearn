import json

with open("file/user.json") as file:
    user = json.load(file)

print(json.dumps(user, indent=4,sort_keys=True))
print(user["name"])
user = {
    "fullname": "John ABC",
    "number": 1234567890
}
with open("file/user_w.json", "w") as file:
    json.dump(user, file, indent=4)