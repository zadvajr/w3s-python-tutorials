#python class and objects

# creating class

class MyClass:
    x = 5
#end

#create object of class MyClass

p1 = MyClass()

print(p1.x)

#end

#the __init_() function used to assign values to object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Zadva", 34)

print(p1.name) # Zadva
print(p1.age) # 34

#end

#the string representation of an object is as follows

print(p1) # <__main__.Person object at 0x000001B09542A6C8>

#Need for __str__() method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = Person("Daniel Zadva Jnr", 34)

print(p1) #Daniel Zadva Jnr (34)

#end

