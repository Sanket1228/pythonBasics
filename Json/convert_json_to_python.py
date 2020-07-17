import json 

x = '{"name":"Sanket","age":30,"city":"Nashik"}'

y = json.loads(x)

print(y["age"])