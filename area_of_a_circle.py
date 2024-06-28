#Python script to calculate the area of a circle
#The formula to calculate the area of a circle is:
#Area = πr^2
#Where π is a constant approximately equal to 3.14159 and r is the radius of the circle.
#The script prompts the user to enter the radius of the circle and calculates the area of the circle using the formula.
#The result is printed to the console.
#The script uses the input() function to read a user input from the console.
#The input() function reads a line from the console and converts it into a string.
#The float() function is used to convert the string to a floating-point number.
#The area is calculated using the formula and printed to the console.
#The script uses the round() function to round the result to two decimal places.
#The round() function takes two arguments: the number to round and the number of decimal places.
#The result is printed to the console using the print() function.
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius**2
rounded_area = round(area, 2)
print("The area of the circle is:", rounded_area)