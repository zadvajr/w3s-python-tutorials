#sort list

family = ["Daniel", "Panazara", "Kefas", "Comfort", "Lakwa", "Hyelafiya", "Fibi", "Vara"]

family.sort()

print(family) # prints: ['Comfort', 'Daniel', 'Fibi', 'Hyelafiya', 'Kefas', 'Lakwa', 'Panazara', 'Vara']
                #prints the sorted list

# sort numbers

integers = [34, 27, 23, 40, 45]

integers.sort()

print(integers) # prints: [23, 27, 34, 40, 45] sorted in ascending order

#sort in descending order as follows

integers.sort(reverse=True) # sorts to descending order

print(integers)

# sort insensitive

names = ["daniel", "ZADVA", "jnr"]

names.sort(key=str.lower) #this line makes sorting insensitive

print(names)

# reverse the order of string

names.reverse()
print(names)

