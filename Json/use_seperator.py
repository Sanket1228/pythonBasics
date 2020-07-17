import json

x = {
    "name" : "Aniket",
    "age" : 40,
    "married" : True,
    "divorced" : False,
    "children" : ("Sandy","Aanny"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW","mpg" : 27.5},
        {"model" : "Ford","mpg": 24.1}
    ]
 }

print(json.dumps(x,indent=4,separators=(",",":")))