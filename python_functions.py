#python functions

#print and call a function

def myfunction():
    print("Hello function")

myfunction()

#end

#function with argument

def hello(name):
    print("Hello! Welcome ", name)

hello("Daniel")

#end

#function with arbitrary arguments

def welcome(*name):
    print("Welcome ", *name)

welcome("daneile", "zadva")

#end

