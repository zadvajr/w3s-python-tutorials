#Python Operators
#Operators are used to perform operations on variables and values.
#Python divides the operators in the following groups:
#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators

#Python Arithmetic Operators
#Arithmetic operators are used with numeric values to perform common mathematical operations:
#+    Addition	x + y
x = 5
y = 3
print(x + y) # Output: 8

#-    Subtraction	x - y
x = 5
y = 3
print(x - y) # Output: 2

#*    Multiplication	x * y
x = 5
y = 3
print(x * y) # Output: 15

#/    Division	x / y
x = 12
y = 3
print(x / y) # Output: 4.0

#%    Modulus	x % y
x = 5
y = 2
print(x % y) # Output: 1

#**    Exponentiation	x ** y
x = 2
y = 5
print(x ** y) # Output: 32

#//    Floor division	x // y
x = 5
y = 2
print(x // y) # Output: 2

#Python Assignment Operators
#Assignment operators are used to assign values to variables:
#=    x = 5    x = 5
x = 5
print(x) # Output: 5

#+=    x += 3    x = x + 3
x = 5
x += 3
print(x) # Output: 8

#-=    x -= 3    x = x - 3
x = 5
x -= 3
print(x) # Output: 2

#*=    x *= 3    x = x * 3
x = 5
x *= 3
print(x) # Output: 15

#/=    x /= 3    x = x / 3
x = 12
x /= 3
print(x) # Output: 4.0

#%=    x %= 3    x = x % 3
x = 5
x %= 3
print(x) # Output: 2

#//=    x //= 3    x = x // 3
x = 5
x //= 3
print(x) # Output: 1

#**=    x **= 3    x = x ** 3
x = 2
x **= 3
print(x) # Output: 8

#&=    x &= 3    x = x & 3
x = 5
x &= 3
print(x) # Output: 1

#|=    x |= 3    x = x | 3
x = 5
x |= 3
print(x) # Output: 7

#^=    x ^= 3    x = x ^ 3
x = 5
x ^= 3
print(x) # Output: 6

#>>=    x >>= 3    x = x >> 3
x = 5
x >>= 3
print(x) # Output: 0

#<<=    x <<= 3    x = x << 3
x = 5
x <<= 3
print(x) # Output: 40

#Python Comparison Operators
#Comparison operators are used to compare two values:
#==    Equal	x == y
x = 5
y = 3
print(x == y) # Output: False

#!=    Not equal	x != y
x = 5
y = 3
print(x != y) # Output: True

#>    Greater than	x > y
x = 5
y = 3
print(x > y) # Output: True

#<    Less than	x < y
x = 5
y = 3
print(x < y) # Output: False

#>=    Greater than or equal to	x >= y
x = 5
y = 3
print(x >= y) # Output: True

#<=    Less than or equal to	x <= y
x = 5
y = 3
print(x <= y) # Output: False

#Python Logical Operators
#Logical operators are used to combine conditional statements:
#and    Returns True if both statements are true	x < 5 and  x < 10
x = 5
print(x > 3 and x < 10) # Output: True

#or    Returns True if one of the statements is true	x < 5 or x < 4
x = 5
print(x < 5 or x < 4) # Output: False

#not    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
x = 5
print(not(x > 3 and x < 10)) # Output: False

#Python Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#is    Returns True if both variables are the same object	x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # Output: True
print(x is y) # Output: False
print(x == y) # Output: True

#is not    Returns True if both variables are not the same object	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) # Output: False
print(x is not y) # Output: True
print(x != y) # Output: False

#Python Membership Operators
#Membership operators are used to test if a sequence is presented in an object:
#in    Returns True if a sequence with the specified value is present in the object	x in y
x = ["apple", "banana"]
print("banana" in x) # Output: True

#not in    Returns True if a sequence with the specified value is not present in the object	x not in y
x = ["apple", "banana"]
print("pineapple" not in x) # Output: True

#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:
#&    AND	Sets each bit to 1 if both bits are 1
print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#|    OR	Sets each bit to 1 if one of two bits is 1
print(6 | 3)


#^    XOR	Sets each bit to 1 if only one of two bits is 1
print(6 ^ 3)

#~    NOT	Inverts all the bits
print(~6)

#<<    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(6 << 3)

#>>    Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(6 >> 3)

#Python Operators Precedence
#The following table lists all operators from highest precedence to lowest.
#Arithmetic operators
#Bitwise shift operators
#Comparison operators
#Bitwise 'AND' operators
#Bitwise 'XOR' operators
#Bitwise 'OR' operators
#Logical 'AND' operators
#Logical 'OR' operators

