#Python - Access List Items
#Access Items
#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Prints the last item in the list - cherry

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Prints the items from the 3rd item to the 5th item

#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #Prints the items from the 4th item to the 2nd item

#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  