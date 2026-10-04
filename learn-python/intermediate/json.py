# Python JSON

# JSON is used to store and send data.

import json


# Create a Python dictionary

user = {
    "name": "Poria",
    "age": 16,
    "language": "Python"
}


# Convert Python data to JSON

json_data = json.dumps(user)

print(json_data)


# Convert JSON back to Python

python_data = json.loads(json_data)

print(python_data["name"])
print(python_data["language"])


# Save JSON to a file

with open("user.json", "w") as file:
    json.dump(user, file)


# Read JSON from a file

with open("user.json", "r") as file:
    data = json.load(file)

print(data)
