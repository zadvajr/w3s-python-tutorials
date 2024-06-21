scores = 0
units = 0

while True:
    score = input("Enter your score (enter 'END' to calculate GP): ")
    if score.upper() == 'END':
        break
    else:
        unit = int(input("How many units is this course? "))
        if score in range(70, 100+1):
            point = 5
        elif score in range(60, 69+1):
            point = 4
        elif score in range(50, 59+1):
            point = 3
        elif score in range(45, 49+1):
            point = 2
        elif score in range(40, 44+1):
            point = 1
        else:
            point = 0
    scores += point
    units += unit

print("Total points: ", scores)
print("Total units: ", units)
print("GPA: ", scores/units)