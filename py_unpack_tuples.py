#Unpack Tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#Example
#Packing a tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple) #Output: ('apple', 'banana', 'cherry')

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
#Example    
#Unpacking a tuple:
thistuple = ("apple", "banana", "cherry")
(green, yellow, red) = thistuple
print(green) #Output: apple
print(yellow) #Output: banana
print(red) #Output: cherry

#This will assign the first item in the tuple to green, the second item to yellow, and the third item to red.

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#Example
#Assign the rest of the values as a list called "red":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
(green, yellow, *red) = thistuple
print(green) #Output: apple
print(yellow) #Output: banana
print(red) #Output: ['cherry', 'orange', 'kiwi', 'melon']

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
#Example
#Add a list of values the "tropic" variable:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
(green, *tropic, red) = thistuple
print(green) #Output: apple
print(tropic) #Output: ['banana', 'cherry', 'orange', 'kiwi']
print(red) #Output: melon

#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
#Note: If you want to unpack a tuple in a function call, use the * operator.
#Example
#Unpack a tuple in a function:
def sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s
print(sum(1, 2, 3)) #Output: 6
print(sum(10, 20, 30, 40)) #Output: 100
print(sum(100, 200, 300, 400, 500)) #Output: 1500
#Output: 6
#Output: 100
#Output: 1500
#Note: The function will receive a tuple of arguments, and return their sum.

#Note: If the number of arguments is unknown, add a * before the parameter name:
#Example
#If the number of arguments is unknown, add a * before the parameter name:
def sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s
print(sum(1, 2, 3)) #Output: 6
print(sum(10, 20, 30, 40)) #Output: 100
print(sum(100, 200, 300, 400, 500)) #Output: 1500
#Output: 6
#Output: 100
#Output: 1500
#Note: The function will receive a tuple of arguments, and return their sum.