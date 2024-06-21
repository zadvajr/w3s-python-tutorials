blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
height = 0
i = 0
while i in range(blocks+1):
    height += 1
    level = 1
    blocks -= level + 1
    level += 1


print("The height of the pyramid:", height)
