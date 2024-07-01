#Python - Tuples
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#Create a Tuple:
fruits = ("apple", "banana", "cherry")

#Tuple items are ordered, unchangeable, and allow duplicate values.

#Tuple Items
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#Unchangeable
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#Allow Duplicates
#Since tuples are indexed, they can have items with the same value:
#Example
#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
#To determine how many items a tuple has, use the len() method:
#Example
#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#Example
#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
#Example
#One item tuple, remember the comma:
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types
#Tuple items can be of any data type:
#Example
#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

#A tuple can contain different data types:
#Example
#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

#type()
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
#Example
#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
#Example
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)