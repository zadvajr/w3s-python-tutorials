# Python code​​​​​​‌​‌​‌‌‌‌‌‌​‌‌​‌‌​‌‌​​‌‌‌‌ below

def factorial(num):
    # Your code goes here.
    if(isinstance(num, int)):
        if(num == 0 or num == 1):
            return 1
        while(num > 1):
            return num * factorial(num - 1)
    else:
        return None
    
print(factorial("jhdksah"))