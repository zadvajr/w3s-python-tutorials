#implementing inheritance in python

#create a parent class called Person
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)

p1 = Person("Daniel", "Zadva Jnr")
p1.printname()

#end parent class

#create a child class called student
#to create a child class you pass the person class as argument when creating the student class

class Student(Person):
    pass # use pass keyword when you don't want to create properties or method of the class

#create object of the class Student and access the printname method inherited from the parent class
p2 = Student("Kefas", "Daniel")
p2.printname() #output: Kefas Daniel

#end

