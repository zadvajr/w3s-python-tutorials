#Python - Sorting Lists
#Sorting Lists
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#Example
#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "apple", "zingby", "cherries", "grapes", "watermelon", "strawberry", "blueberry", "raspberry", "blackberry", "peach", "plum", "pear", "apricot", "nectarine", "pomegranate", "fig", "date", "coconut", "lychee", "guava", "papaya", "passionfruit", "dragonfruit", "kiwano", "starfruit", "mangosteen", "durian", "jackfruit", "rambutan", "longan", "lychee", "carambola", "persimmon", "quince", "tamarillo", "tamarind", "ugli", "yuzu", "kumquat", "loquat", "pawpaw", "soursop", "sugar-apple", "santol", "sapodilla", "salak", "rambutan", "mangosteen", "longan", "lychee", "carambola", "persimmon", "quince", "tamarillo", "tamarind", "ugli", "yuzu", "kumquat", "loquat", "pawpaw", "soursop", "sugar-apple", "santol", "sapodilla", "salak"]
thislist.sort()
# print(thislist)
for x in thislist:
  print(x)

#Sort the list numerically:
#Example
#Sort the list numerically:
thislist = [100, 50, 65, 82, 23, 12, 34, 56, 78, 90]
thislist.sort()
print(thislist)

#Sort the list descending:
#Example
#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "apple"]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):
#Example
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#Example
#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#But you can use the key casefold to do a case-insensitive sort:
#Example
#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.casefold)
print(thislist)

#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
#Example
#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Sort the list by the length of the values:
#Example
#Sort the list by the length of the values:
def myfunc(n):
  return len(n)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myfunc)
print(cars)
#Sort the list by the length of the values and reversed:
#Example
#Sort the list by the length of the values and reversed:
def myfunc(n):
  return len(n)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myfunc)
print(cars)