#python dictionary

#creates dictionary mydict
mydict= {
    "name": "Daniel",
    "age": 32,
    "height": 1.7
}

#retrieve value from mydict
print(mydict['name'])

#add item to mydict
mydict["level"] = "medium"
print(mydict)

#update item
mydict["age"] = 35
print(mydict["age"])

#delete item in a dictionary
del mydict["level"]
print(mydict)

#find the length of mydict
print(len(mydict))

#loop through mydict
for key in mydict:
    print(key, ": ", mydict[key])

#check whether key exits in mydict
print('age' in mydict) #prints True

#checks whether key not in mydict
print('age' not in mydict) #prints False

#dictionary methods
#keys() - returns keys in mydict
print(mydict.keys())

#values() - returns values in mydict
print(mydict.values())

#get() - gets keys
print(mydict.get('age'))

#pop(key) 
print(mydict.pop('name'))

#popitem() removes random key in a dictionary
print(mydict.popitem())

mydict.clear() #clears everythin in mydict
print(mydict)