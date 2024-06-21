#this two lines creates a file "mytext.txt" with the data "Learning Python is cool"
with open("mytext.txt", 'w') as f:
    f.write("Learning python is cool")

#this two lines reads data from a file "mytext.txt"
with open("mytext.txt") as f:
    print(f.read())