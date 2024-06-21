#access dictionary item
#you can access dictionary items by using square brackets

favorite_car = {
    "brand": "BMW",
    "model": "LE23",
    "year": [2023, 2024]
}

print("My favorite car is ", favorite_car["brand"], favorite_car["model"], "make and release year is ", favorite_car["year"][0], "or ", favorite_car["year"][1])

#end

#you can also use get() method to access dictionary item as follow

print(favorite_car.get("model"))

#end

#get a list of all the keys in a dictionary as follows
x = favorite_car.keys()
print(x)

#end

#add items to a dictionary

favorite_car["color"] = "Black"

print(favorite_car)

#end

#get list of dictionary values

x = favorite_car.values()

print(x)

#end

#change values in a dictionary

favorite_car["year"] = 2024

print(favorite_car)

#end

