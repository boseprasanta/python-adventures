myMap = {}

myMap = {
    "name": "John",
    "age": 30,
    "city": "New York"  
}


myMap["age"] = 31 # update

print(myMap["name"]) # John

print("name" in myMap) # True

print("printing keys")

for key in myMap:
    print("key =", key)

print("printing values")

for value in myMap.values():
    print("value =", value)

print("printing items and values")

for key, value in myMap.items():
    print("key =", key, "value =", value)