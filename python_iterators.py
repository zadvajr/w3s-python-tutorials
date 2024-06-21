#PYTHON ITERATORS
# An Iterator - is an object that contains countable number of values
# it also means an object that you can be iterated upon or traversed the values
# in python an iterator is an object which implements iterator protocol which has two methods
# __iter__() and __next__()
# Lists, Tuples, Sets, Dictionary are all iterable objects
# all the above mentioned has iter() and next() methods

#examples

mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit)) # apple
print(next(myit)) # banana
print(next(myit)) # cherry

#strings too are iterators they can return an iterator

mystr = "banana"
myiter = iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#Looping through an iterator
#we can loop through an iterator using for loop
myfruits = ["apple", "banana", "cherry", "orange"]

for fruit in myfruits:
    print(fruit)


#iterate the characters in a string
name = "daniel"
for i in name:
    print(i)

### Create an Iterator
