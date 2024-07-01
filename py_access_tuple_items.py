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