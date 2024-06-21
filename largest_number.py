#python script to find the largest of numbers entered by the user

largest_number = -999999999

number = int(input("Enter a number or -1 to Quit: "))

while number != -1:
    if number > largest_number:
        largest_number = number

    number = int(input("Enter a number or -1 to Quit: "))
print("The largest of the numbers you entered: ", largest_number)