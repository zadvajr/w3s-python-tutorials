#python objects

class Person:
    
    #constructor or initializer
    def __init__(self, name):
        self.name = name
    
    def whoami(self):
        return "You are " + self.name

p1 = Person("Tomi")

print(p1.whoami())
print(p1.name)

#update name
p1.name = "Jerry"

print(p1.name)  #will output: Jerry
print(p1.whoami()) #will output: You are Jerry


