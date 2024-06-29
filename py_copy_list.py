#Python - Copy Lists
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

#Insert the copy() method to make a copy of a list, and the list() method to make a copy of a list, but there are other ways to make a copy of a list:
#Example
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#Now the mylist has the same content as thislist:
#Example
#Print the list items of the original list:
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Print the list items of the copied list:
mylist = thislist.copy()
print(mylist)

#The list is now copied and any changes made to the original list will not affect the copied list:
#Example
#Make changes to the original list:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Print the original list:
print(thislist)
#Print the copied list:
print(mylist)
#The original list has been changed, but the copied list is still the same.

