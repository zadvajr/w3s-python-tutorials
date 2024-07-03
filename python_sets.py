#Python Sets
myset = {"apple", "banana", "cherry"}

#Set
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
#Example
#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) #Output: {'apple', 'banana', 'cherry'}

#Note: Sets are unordered, so you cannot be sure in which order the items will appear.

#Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Unordered
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Unchangable
#Sets are unchangable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.

#Duplicates Not Allowed
#Sets cannot have two items with the same value.
#Example
#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #Output: {'apple', 'banana', 'cherry'}

#Get the Length of a Set
#To determine how many items a set has, use the len() method.
#Example
#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #Output: 3

#Set Items - Data Types
#Set items can be of any data type:
#Example
#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1) #Output: {'apple', 'banana', 'cherry'}
print(set2) #Output: {1, 3, 5, 7, 9}
print(set3) #Output: {False, True}

#A set can contain different data types:
#Example
#A set with strings, integers and boolean values:
set1 = {"abc", 34, True }
print(set1) #Output: {34, 'abc\n', True}

#type()
#From Python's perspective, sets are defined as objects with the data type 'set':
#Example
#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset)) #Output: <class 'set'>

#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Example
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #Output: {'apple', 'banana', 'cherry'}

#Note: The set() constructor can also be used to make a set.
#Note: If the constructor is called without arguments, it will return an empty set.

