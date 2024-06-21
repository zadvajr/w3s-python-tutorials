#looping through a tuple

thistuple = ("Apple", "Banana", "Cherry", "Strawberry")

txt = "-"
#loop through tuple using for
for item in thistuple:
    print(item)

print(txt.center(50, '-'))

#using index
for i in range(len(thistuple)):
    print(thistuple[i])

print(txt.center(50, '-'))

#using while loop

i = 0

while i < len(thistuple):
    print(thistuple[i])
    i = i +1

print(txt.center(50, '-'))
