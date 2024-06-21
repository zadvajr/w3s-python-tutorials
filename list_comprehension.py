#python list comprehension
# is a method of generating a new list from existing list
# check the example below

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#new list odd based of the integers numbers
odd = [x for x in integers if(x % 2 != 0)] # list comprehension to extract odd numbers from given list of natural nubmers

print(odd)

even = [x for x in integers if(x % 2 == 0)]  #extracts even numbers

# syntax: newlist = [expression for item in iterable if condition == True]

print(even)

multiplybyten = [(x * 10) for x in integers]

print(multiplybyten)