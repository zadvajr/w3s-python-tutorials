# __str__() function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

p1 = Person("Zadva", 35)

print(p1)