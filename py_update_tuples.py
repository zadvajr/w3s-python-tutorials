#Update Tuples
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

#Change Tuple Values
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#Example
#Convert the tuple into a list to be able to change it:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple) #Output: ('apple', 'kiwi', 'cherry')

#Add Items
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple. 
#Example
#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #Output: ('apple', 'banana', 'cherry', 'orange')

#2. Add tuple to a tuple. You can add one tuple to another by using the + operator.
#Example
#Create a new tuple as in the following example:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) #Output: ('a', 'b', 'c', 1, 2, 3)

#Remove Items
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
#1. Convert the tuple into a list, remove the item, and convert it back into a tuple.
#Example
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #Output: ('banana', 'cherry')

#2. The del keyword can delete the tuple completely:
#Example
#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #This will raise an error because the tuple no longer exists
#Output: NameError: name 'thistuple' is not defined