#Loop Tuples
#You can loop through the tuple items by using a for loop.
#Example
#Iterate through the tuple items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x) #Output: apple, banana, cherry

#Loop Through the Index Numbers
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#Example
#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i]) #Output: apple, banana, cherry 

#Using a While Loop
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
#Remember to increase the index by 1 after each iteration.
#Example
#Loop through the list items by using a while loop:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i]) #Output: apple, banana, cherry
    i = i + 1

#Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through a tuple.
#Example
#A short hand for loop that will print all items in a tuple:
thistuple = ("apple", "banana", "cherry")
[print(x) for x in thistuple] #Output: apple, banana, cherry
#Note: The list comprehension method is more efficient and more readable, as it is a single line of code.   
