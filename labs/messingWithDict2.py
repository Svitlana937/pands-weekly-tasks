car = {
    "make" : "Fiat",
    "model" : "Punto",
    "price"  : 10000,
    "tags" : ["pre-owner", "Best Buy", "Dealer"]
}
# print(car)
# print(car["tags"])

for key in car:
    print(key)
    print(car[key])
    print("")
    print(key, 'has value', car[key])

for key, value in car.items():
    print(key+  'has value', value)
