#Python - Access Set Items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
#Example
#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#Output: apple, banana, cherry
#Example
#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#Output: True
#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#Add Items
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.
#Example
#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) #Output: {'apple', 'banana', 'cherry', 'orange'}
#Example
#Add multiple items to a set, using the update() method:
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset) #Output: {'apple', 'banana', 'cherry', 'grapes', 'mango', 'orange'}

#Get the Length of a Set
#To determine how many items a set has, use the len() method.
#Example
#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #Output: 3

#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
#Example
#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #Output: {'apple', 'cherry'}
#Note: If the item to remove does not exist, remove() will raise an error.
#Example
#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #Output: {'apple', 'cherry'}
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
#Example
#Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #Output: cherry
print(thisset) #Output: {'apple', 'banana'}
#Example
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #Output: set()
#Example
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #Output: NameError: name 'thisset' is not defined
#Example
#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Example
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #Output: {'apple', 'banana', 'cherry'}
#Example
#Join Two Sets
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
#Example
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #Output: {1, 2, 3, 'a', 'b', 'c'}
#Example
#The update() method inserts all the items from one set into another:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) #Output: {1, 2, 3, 'a', 'b', 'c'}
#Note: Both union() and update() will exclude any duplicate items.
#There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates, check the full list of set methods in the bottom of this page.
#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Example
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #Output: {'apple', 'banana', 'cherry'}
#Note: The set() constructor can also be used to make a set.
#Note: If the constructor is called without arguments, it will return an empty set.
#Python - Loop Sets
#Loop Items
#You can loop through the set items by using a for loop:
#Example
#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#Output: apple, banana, cherry
#Example
#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#Output: True
#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#Add Items
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.
#Example
#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) #Output: {'apple', 'banana', 'cherry', 'orange'}
#Example
#Add multiple items to a set, using the update() method:
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset) #Output: {'apple', 'banana', 'cherry', 'grapes', 'mango', 'orange'}

#Get the Length of a Set
#To determine how many items a set has, use the len() method.
#Example
#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #Output: 3

#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
#Example
#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #Output: {'apple', 'cherry'}

#Note: If the item to remove does not exist, remove() will raise an error.
#Example
#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #Output: {'apple', 'cherry'}
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
#Example
#Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #Output: cherry
print(thisset) #Output: {'apple', 'banana'}
#Example
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #Output: set()
#Example
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #Output: NameError: name 'thisset' is not defined
#Example
#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Example
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #Output: {'apple', 'banana', 'cherry'}
#Example
#Join Two Sets

#There are several ways to join two or more sets in Python. You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
#Example
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #Output: {1, 2, 3, 'a', 'b', 'c'}
