#Python - Add Dictionary Items
#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#Example
#Add a color item to the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict) #Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#Note: There is no specific order for dictionaries.
#Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.