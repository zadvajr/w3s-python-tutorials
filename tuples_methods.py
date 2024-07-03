#Tuples methods
#Python has two built-in methods that you can use on tuples.
#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found
#Example
#Using the count() method:
#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) #Output: 2

#Example
#Using the index() method:
#Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) #Output: 3

#Note: The index() method only returns the first occurrence of the value.
#Note: If the item does not exist, value error is raised.