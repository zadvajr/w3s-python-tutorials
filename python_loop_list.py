#Python - Loop List
#Loop Through a List
#You can loop through the list items by using a for loop.
#For Example:
#Print all items in the list, one by one
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#The for loop does not require an indexing variable to set beforehand.

#Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#For Example:
#Print all items by referring to their index number
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
  print(fruits[i])

#The len() function returns the length of the list.
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

#Using a While Loop
#You can loop through the list items by using a while loop.
#For Example:
#Print all items in the list, one by one
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1

#The while loop requires relevant variables to be ready beforehand.

#Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists.
#For Example:
#A short hand for loop that will print all items in the list
fruits = ["apple", "banana", "cherry"]
[print(x) for x in fruits]

#List Comprehension does not allow for conditions or statements.