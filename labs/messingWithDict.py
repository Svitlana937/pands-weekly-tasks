# messing with dictionaries

car = {
    "make" : "Ford",
    "model" : "Mustang",
    "year"  : 2006,
    "owner" : {
        "name" : "Andrew",
        "driver-number" : 1123
    }
}
attr = "owner"
print(car[attr])
print(car["owner"]["name"])
print(type(car["owner"].get("names")))