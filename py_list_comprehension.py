#Python - List Comprehension
#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#For Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

#For Example:
#Create a new list with only fruits containing the letter "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) #Prints the new list of fruits: apple, banana, mango

#With list comprehension you can do all that with only one line of code:
#For Example:
#Create a new list with only fruits containing the letter "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #Prints the new list of fruits: apple, banana, mango

#The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.
#Expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
#The item is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
#The iterable can be any iterable object, like a list, tuple, set etc.
#The condition is like a filter that only accepts the items that evaluate to True.
#The condition is optional and can be omitted.

#Without the condition, the list comprehension will include all items in the iterable.
#For Example:
#Return the item if it is not an apple
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist) #Prints the new list of fruits: banana, cherry, kiwi, mango

#The condition if x != "apple" will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:
#For Example:
#With no if statement
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]   
print(newlist) #Prints the new list of fruits: apple, banana, cherry, kiwi, mango

#If you want to modify the items in the list, you can add an expression:
#For Example:
#Set the values in the new list to upper case
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) #Prints the new list of fruits: APPLE, BANANA, CHERRY, KIWI, MANGO

#You can set the outcome to whatever you like:
#For Example:
#Set all values in the new list to 'hello'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist) #Prints the new list of fruits: hello, hello, hello, hello, hello

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#For Example:
#Return 'orange' instead of 'banana'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #Prints the new list of fruits: apple, orange, cherry, kiwi, mango

#The expression in the example above says:
#Return the item if it is not banana, if it is banana return orange.
#You can have multiple conditions if you like:
#For Example:
#Return 'hello' if the item is 'banana', otherwise return the item itself
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "hello" for x in fruits]
print(newlist) #Prints the new list of fruits: apple, hello, cherry, kiwi, mango

#The expression can also contain functions:
#For Example:
#Take the first character of each word and set the outcome to upper case
def myfunc(n):
  return n[0].upper() + n[1:]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [myfunc(x) for x in fruits]
print(newlist) #Prints the new list of fruits: Apple, Banana, Cherry, Kiwi, Mango

#You can use functions to produce the values in the new list:
#For Example:
#Create a function that produces a sequence of numbers
def myfunc(n):
  return len(n)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [myfunc(x) for x in fruits]
print(newlist) #Prints the new list of fruits: 5, 6, 6, 4, 5

#You can use functions to filter the result:
#For Example:
#Only return items with enough characters
def myfunc(n):
  return len(n) > 5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if myfunc(x)]
print(newlist) #Prints the new list of fruits: banana, cherry, mango

#The filter function can be omitted, leaving only the expression:
#For Example:
#With no filter
def myfunc(n):
  return len(n) > 5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) #Prints the new list of fruits: apple, banana, cherry, kiwi, mango
#The outcome is a new list, leaving the old list unchanged.
#The iterable can be any iterable object, like a list, tuple, set etc.
#The condition is optional and can be omitted.
#Without the condition, the list comprehension will include all items in the iterable.
#The condition is like a filter that only accepts the items that evaluate to True.
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
#The return value is a new list, leaving the old list unchanged.
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome.
#The expression can also contain functions.
#The expression can also contain functions to filter the result.
#The expression can also contain functions to produce the values in the new list.