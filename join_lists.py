# join lists
# there are different ways to join lists

#1: using + opereator

names = ["daniel", "ishaku", "andy"]
age = [34, 45, 40]

names_age = names + age

print(names_age) # ['daniel', 'ishaku', 'andy', 34, 45, 40]

#2: by appending list items 

for x in age:
    names.append(x)

print(names) # prints: ['daniel', 'ishaku', 'andy', 34, 45, 40]

#3: using extend() method
names.extend([1,2,3])
print(names) # prints: ['daniel', 'ishaku', 'andy', 34, 45, 40, 1, 2, 3]
