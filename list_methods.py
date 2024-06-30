#List Methods
#Python has a set of built-in methods that you can use on lists.
#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#Append Items
#To add an item to the end of the list, use the append() method:
#Example
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an element to the list at the specified index.
#Example
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
#To append elements from another list to the current list, use the extend() method.
#Example
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Example
#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove Specified Item
#The remove() method removes the first occurrence of the item with the specified value.
#Example
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The remove() method raises an error when the specified item does not exist.
#Example
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.
#Example
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
#Example
#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()

#The del keyword also removes the specified index:
#Example
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#Example
#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.
#Example
#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
#Example
#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
#Example
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

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

#The list() Constructor
#It is also possible to use the list() constructor to make a new list.
#Example
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)