#Python - Remove Dictionary Items
#Removing Items
#There are several methods to remove items from a dictionary:
#Example
#The pop() method removes the item with the specified key name:
#Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict) #Output: {'brand': 'Ford', 'year': 1964}

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
#Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict) #Output: {'brand': 'Ford', 'model': 'Mustang'}

#The del keyword removes the item with the specified key name:
#Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict) #Output: {'brand': 'Ford', 'year': 1964}

#The del keyword can also delete the dictionary completely:
#Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# print(thisdict) #Output: NameError: name 'thisdict' is not defined

#The clear() method empties the dictionary:
#Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict) #Output: {}