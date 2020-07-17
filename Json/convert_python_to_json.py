import json

x = {
    "name" : "Sanket",
    "age" : 20,
    "city" : "Nashik"
}

y = json.dumps(x)

print(y)