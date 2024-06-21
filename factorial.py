#python code to compute a factorial of a number n

user_input = input("Enter a Number: ")

number = int(user_input)

def factorial(n):
    if(n == 0 or n ==1):
        return 1
    while(n > 1):
        return n * factorial(n-1)

print("The factorial of ", number, " = ", factorial(number))