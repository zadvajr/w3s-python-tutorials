#String methods
# 1. capitalize() - Converts the first character to upper case
txt = "python"
x = txt.capitalize()
print(x) # Output: Python

# 2. casefold() - Converts string into lower case
txt = "PYTHON"
x = txt.casefold()
print(x) # Output: python

# 3. center() - Returns a centered string
txt = "Python"
x = txt.center(20)
print(x) # Output: '       Python       '

# 4. count() - Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) # Output: 2

# 5. encode() - Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x) # Output: b'My name is St\xc3\xa5le'

# 6. endswith() - Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) # Output: True

# 7. expandtabs() - Sets the tab size of the string
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x) # Output: H e l l o

# 8. find() - Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # Output: 7

# 9. format() - Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) # Output: For only 49.00 dollars!

# 10. format_map() - Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format_map({"price": 49})) # Output: For only 49.00 dollars!

# 11. index() - Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) # Output: 7

# 12. isalnum() - Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x) # Output: True

# 13. isalpha() - Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x) # Output: True

# 14. isdecimal() - Returns True if all characters in the string are decimals
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x) # Output: True

# 15. isdigit() - Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x) # Output: True

# 16. isidentifier() - Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x) # Output: True

# 17. islower() - Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x) # Output: True

# 18. isnumeric() - Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x) # Output: True

# 19. isprintable() - Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) # Output: True

# 20. isspace() - Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x) # Output: True

# 21. istitle() - Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) # Output: True

# 22. isupper() - Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) # Output: True

# 23. join() - Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) # Output: John#Peter#Vicky

# 24. ljust() - Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") # Output: banana               is my favorite fruit.

# 25. lower() - Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x) # Output: hello my friends

# 26. lstrip() - Returns a left trim version of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite") # Output: of all fruits banana      is my favorite
