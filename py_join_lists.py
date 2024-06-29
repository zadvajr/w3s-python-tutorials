#Python - Join Lists
#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
#Example
#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Another way to join two lists are by appending all the items from list2 into list1, one by one:
#Example
#Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#Or you can use the extend() method, which purpose is to add elements from one list to another list:
#Example
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#Note: The list1 will be modified after a call to list1.extend(list2).
#The list2 will remain unchanged.
#Append Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

#Example
#Add elements of a tuple to a list:
list1 = ["a", "b", "c"]
tuple1 = ("d", "e", "f")
list1.extend(tuple1)
print(list1)
#Add elements of a set to a list:
list1 = ["a", "b", "c"]
set1 = {"d", "e", "f"}
list1.extend(set1)
print(list1)
#Add elements of a dictionary to a list:
list1 = ["a", "b", "c"]
dict1 = {"name": "John", "country": "Norway"}
list1.extend(dict1)
print(list1)
#Note: When using extend(), all elements from the iterable object are added to the list.
#Example
#Add elements of a set to a list:
list1 = ["a", "b", "c"]
set1 = {"d", "e", "f"}
list1.extend(set1)
print(list1)
#Add elements of a dictionary to a list:
list1 = ["a", "b", "c"]
dict1 = {"name": "John", "country": "Norway"}
list1.extend(dict1)
print(list1)
#Note: When using extend(), all elements from the iterable object are added to the list.
#The list1 will be modified after a call to list1.extend(set1) and list1.extend(dict1).
#The set1 and dict1 will remain unchanged.
#The list() Constructor
#It is also possible to use the list() constructor to make a new list.
#Example
#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)