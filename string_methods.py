#python strings method

#capitalize() method: this converts the first letter of a string to capital letter
txt = "daniel zadva jnr"

print(txt.capitalize()) # Prints "Daniel zadva jnr"

#end capitalize() method here

#casefold() method: converts strings into lower case

txt = "DANIEL ZADVA JNR"

print(txt.casefold()) # prints "daniel zadva jnr"

#end casefold() method here

#center() method: returns a centered strings

txt = "daniel zadva jnr"

print(txt.center(50, "-")) #prints -----------------daniel zadva jnr-----------------
                            #center() takes one or two arguments, 
                            #the first 50 is the length while the - 
                            # the character to fill the space with txt centered
                            #string.center(length, character)
#end of center()

#count() method: returns the number of times a specified value occurs in a string

txt = "hello hello how have you been? I hope you are doing well?"

print(txt.count("hello")) # prints 2
                        # string.count(value, start, end)

#end of count()

#encode() method: this returns an encoded version of a string

txt = "daniel zadva jnr"

print(txt.encode(encoding="utf-8", errors="backslashreplace"))

# string.encode(encoding=encoding, errors=errors)

# end encode()

#