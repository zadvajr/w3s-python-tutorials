#unpacking tuples

#you can unpack tuples just like list

thistuple = ("Apple", "Banana", "Cherry")

#unpacking
(green, yellow, red) = thistuple

print(green) # Apple
print(yellow) # Banana
print(red) # Cherry

# note that the number of variables must equal the number of item in a tuple
# or you add asterik to a variable to collect the remaining items as a list

(green, *red) = thistuple
print(green) # Apple
print(red) # ['Banana', 'Cherry']

#end