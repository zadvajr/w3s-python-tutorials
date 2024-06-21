#python lists

myfruits = ["apple", "banana", "chery"]

print(myfruits) # prints ["apple", "banana", "chery"]

print(len(myfruits)) # prints 3

#access list items

print(myfruits[2]) # prints chery
print(myfruits[-2]) # prints banana negative indexing

#change list items

myfruits[1] = "Orange"

print(myfruits) #prints ['apple', 'Orange', 'chery']

#insert item into a list in a specified index

myfruits.insert(1, "apple")
print(myfruits) # ['apple', 'apple', 'Orange', 'chery']

#append list items to the end of the list

myfruits.append("citrus") #append() only takes a single argument

print(myfruits) # ['apple', 'apple', 'Orange', 'chery', 'citrus']


#extend() list method

favefruits = ["Mango", "Guava"]

myfruits.extend(favefruits)

print(myfruits) # prints ['apple', 'apple', 'Orange', 'chery', 'citrus', 'Mango', 'Guava']

#remove list items

myfruits.remove("chery")

print(myfruits) #['apple', 'apple', 'Orange', 'citrus', 'Mango', 'Guava'] 

# remove specified index with pop()
#and if no index is provided for pop() the last item is removed

myfruits.pop(-1) # removes last item in a list

print(myfruits) # ['apple', 'apple', 'Orange', 'citrus', 'Mango']

myfruits.pop()

print(myfruits) # ['apple', 'apple', 'Orange', 'citrus']

# delete list items

del myfruits[0] # deletes item at index 0 which is apple

print(myfruits) # ['apple', 'Orange', 'citrus']

# empty a list with clear() method

myfruits.clear()

print(myfruits) # [] empty list

#delete list entirely

del myfruits

print(myfruits) # produces errors