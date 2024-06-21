#update tuples
#tuples are immutable meaning they cannot be changed once created
#in order to change tuple, update or remove items in a tuple
# you need to convert it to a list, make your changes and convert it back to tuple
#check the following examples

favorite_fruits = ("Apple", "Banana", "Pineapple", "Orange", "Mango")

#to change element at index 0 do the following
new = list(favorite_fruits) #converts tuple to list
print(new) # tuple converted to list 

#now update the list as follows
new[0] = "Strawberry"
print(new)

#convert new to tuple
favorite_fruits = tuple(new)

print(favorite_fruits)  # ('Strawberry', 'Banana', 'Pineapple', 'Orange', 'Mango')

#add element to tuple
#to add element to a tuple first convert it to a list
new = list(favorite_fruits)
new.append("Cashew")

#convert back
favorite_fruits = tuple(new)
print(favorite_fruits) #('Strawberry', 'Banana', 'Pineapple', 'Orange', 'Mango', 'Cashew')

#the same method applies to remove items from tuple
