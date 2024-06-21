# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

number = int(input("Enter a Number or Type 0 to Stop the Program: "))

while number:
    if number % 2:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Enter a Number or Type 0 to Stop the Program: "))

print("Odd Numbers Count: ", odd_numbers)
print("Even Numbers Count: ", even_numbers)