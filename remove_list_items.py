#Remove List Items
#Remove specified Item
#The remove() method removes the specified item.
#For Example:
#Remove 'banana' from the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.remove("banana")
print(fruits) #Prints the updated list of fruits: apple, cherry
#If the item to remove does not exist, remove() will raise an error.
#remove the first occurence of 'banana' from the list of fruits
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits) #Prints the list of fruits: apple, banana, cherry, banana
fruits.remove("banana")
print(fruits) #Prints the updated list of fruits: apple, cherry, banana

#Remove Specified Index
#The pop() method removes the specified index.
#For Example:
#Remove the second item from the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.pop(1)
print(fruits) #Prints the updated list of fruits: apple, cherry
#If you do not specify the index, the pop() method removes the last item.
#For Example:
#Remove the last item from the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.pop()
print(fruits) #Prints the updated list of fruits: apple, banana
#If the index does not exist, pop() will raise an error.
#Remove the second item from the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.pop(3)

#The del keyword also removes the specified index:
#For Example:
#Remove the second item from the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
del fruits[1]
print(fruits) #Prints the updated list of fruits: apple, cherry
#If you do not know the index of the item you want to remove, you can use the remove() method.
#For Example:
#Remove 'banana' from the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.remove("banana")
print(fruits) #Prints the updated list of fruits: apple, cherry
#The remove() method removes the specified item.
#If the item to remove does not exist, remove() will raise an error.

#del keyword can also delete the list permanently
#For Example:
#Delete the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
del fruits
print(fruits) #Prints an error message

#Clear the List
#The clear() method empties the list.
#For Example:
#Clear the list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.clear()
print(fruits) #Prints an empty list
