# Python code​​​​​​‌​‌​‌‌‌‌‌​​​‌‌‌‌‌​​‌‌​​‌​ below
def is_palindrome(teststr):
    # Your code goes here.
    strlow = teststr.lower()
    temp = ""
    for str in strlow:
        if(str.isalnum()):
            temp += str
            
    revstr = temp[::-1]

    if(temp == revstr):
        return True
    else:
        return False