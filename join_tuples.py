#Join Tuples
#To join two or more tuples you can use the + operator:
#Example
#Join two tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) #Output: ('a', 'b', 'c', 1, 2, 3)

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
#Example
#Multiply the content of the tuple:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
#Note: You cannot combine a tuple with a list, or two lists, or a list with a string etc. You can only combine tuples with tuples, and lists with lists.
#Note: When you multiply a tuple with a number, it will return a new tuple with repeated items.
#Note: To join two or more lists you can use the + operator.
#Note: To multiply a list you can use the * operator.
#Note: The * operator can be used to multiply any sequence (not just tuples).
