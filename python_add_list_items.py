#Python - Add List Item
#To add an item to the end of the list, use the append() method:
#For Example:
fruits = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.append("orange") #Adds the fruit orange to the list
print(fruits) #Prints the updated list of fruits: apple, banana, cherry, orange

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
#For Example:
fruits  = ["apple", "banana", "cherry"]
print(fruits) #Prints the list of fruits: apple, banana, cherry
fruits.insert(0, "orange") #Adds the fruit orange to the list at index 0
print(fruits) #Prints the updated list of fruits: orange, apple, banana, cherry

#Extend List
#To add elements of another list to the current list, use the extend() method.
#For Example:
food = ["apple", "banana", "cherry"]
meats = ["beef", "chicken", "pork"]
food.extend(meats)
print(food) #Prints the updated list of food: apple, banana, cherry, beef, chicken, pork

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#For Example:
food = ["apple", "banana", "cherry"]
tuple = ("beef", "chicken", "pork")
food.extend(tuple)
print(food) #Prints the updated list of food: apple, banana, cherry, beef, chicken, pork