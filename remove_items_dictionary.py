#Remove Items in a Dictionary

#using pop() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#pop items remove the items with the specified key name

thisdict.pop("year")

print(thisdict)
#end

#using popitem() method - removes the last inserted item

thisdict.popitem()

print(thisdict)

#end

