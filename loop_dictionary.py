#Python - Loop Dictionaries
#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#Example
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x) #Output: brand, model, year
#Loop Through Both Keys and Values

#You can also use the items() method to return the keys and values of a dictionary.
#Example
#Return the keys and values of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():
    print(x, y) #Output: brand Ford, model Mustang, year 1964

#Note: The items() method will return each item in a dictionary, as tuples in a list.
#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword.
#Example
#Check if "model" is present in the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary") #Output: Yes, 'model' is one of the keys in the thisdict dictionary
#Dictionary Length
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
#Example
#Print the number of items in the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict)) #Output: 3
