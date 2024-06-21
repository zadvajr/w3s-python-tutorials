#access tuple items

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

#you can access tuple items using index
print(thistuple[3]) # prints orange

#you can also access it with negative index as follows
print(thistuple[-1]) # prints the last item in a tuple which is mango

#prints range of items with index
print(thistuple[2:5]) #prints items at index 2 to 5 not including the last element
                        #output will be cherry, orange and kiwi  as a tuple

#check if item exist in a tuple

if "apple" in thistuple:
    print("Yes, apple is in this tuple")
else:
    print("No, apple not found in this tuple")