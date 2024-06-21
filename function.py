#python global variable is a variable declared outside of all functional blocks
x = "awesome" #global variable

def myFunc():
    x = "fantastic" #local variable
    print("Python is ", x)

myFunc()
print("Python is ", x)
