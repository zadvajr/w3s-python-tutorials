#python inheritance
#inheritance allow us to define a class that inherits properties and methods from another class
#properties - are variables that belong to that class
# methods - are functions that belong to that class

#parent class or base class - the class being inherited from
# child class or derived class - is the class that inherits the parent
# any class can be a parent or child class, the syntax is the same.

# creating parent class called Person with two properties firstname and lastname, and a method printname

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

#the following line create an object p and calls the printname methodd on it.
p = Person("Daniel", "Zadva Jnr") #create object p 
p.printname() # executes the printname method on the object. 


""""
#INHERITANCE
#to create a class that inherits the Person class check the following

class Student(Person): # you pass in the class to be inherited
    pass #pass will allow you not to define properties or methods for this very class

#create an object instance of student let say x

x = Student("Mary", "Daniel") # object of Student class

#execute the printname method inherited from Person 

x.printname() # will print Mary Daniel

"""

#adding the __init__() function to the child or derived class.
# I have commented out the Ineritance section to demonstrate this
# we want to add the properties and method to the child class instead of the parents' own

class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        self.fname = fname
        self.lname = lname
        #when you define __init__() function for the child class it no longer inherit the init of its parent
        # to keep the inheritance of the parent's __init__() function you add the call to the parent's __init__() functions as follows
        
        # Person.__init__(self, fname, lname)

        #you can also use super() function for the same reason
        super().__init__(fname, lname)

        #add properties
        self.graduationyear = 2025

    #add methods
    def welcome(self):
        print("Welcome", self.fname, self.lname, " to the class of ", self.graduationyear)

x = Student("Mary", "Daniel", 2027)
x.printname()
x.welcome()


#if you add a method in the child class with the same name as a function in the parent class.
# the parent class function will be overriden by the child's
