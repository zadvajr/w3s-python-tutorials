#python code to compute quadratic equations
import math
a = int(input("Enter constant a:"))
b = int(input("Enter constant b:"))
c = int(input("Enter constant c:"))

x1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
x2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)

print("x = ", x1, " or x = ", x2)