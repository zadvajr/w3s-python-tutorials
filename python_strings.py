#string in python are created by enclosing characters in quotes. Python allows for either pairs of single or double quotes.
#you can display a string literal with the print() function
print("Hello, World!")

#assign string to a variable
a = "hello"
print(a)

#multiline strings
#you can assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

#strings are arrays
#strings in python are arrays of bytes representing unicode characters
#square brackets can be used to access elements of the string
a = "Hello, World!"
print(a[1]) #output: e

#loop through string
name = "daniel"
for x in name:
    print(x)

#string length
#to get the length of a string, use the len() function
text = "this is a string text"
print(len(text)) #output: 21