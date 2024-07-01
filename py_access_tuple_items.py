#Python - Access Tuple Items
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
#Example
#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #Output: banana
#Note: The first item has index 0.

#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
#Example
#Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #Output: cherry

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#Example
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #Output: ('cherry', 'orange', 'kiwi')

#Note: The search will start at index 2 (included) and end at index 5 (not included).

#Range of Negative Indexes