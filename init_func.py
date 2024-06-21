#the __init__() function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Daniel", 35)

print(p1.name)
print(p1.age)