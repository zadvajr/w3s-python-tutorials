#modify strings
#uppercase
name = "daniel zadva jnr"
print(name.upper()) #output: DANIEL ZADVA JNR

#lowercase
name = "DANIEL ZADVA JNR"
print(name.lower()) #output: daniel zadva jnr

#remove whitespace
name = "     daniel zadva jnr    "
print(name.strip()) #output: daniel zadva jnr

#replace string
name = "daniel zadva jnr"
print(name.replace("zadva", "zadva, jnr")) #output: daniel zadva, jnr

#split string
name = "daniel zadva jnr"
print(name.split(" ")) #output: ['daniel', 'zadva', 'jnr']

#string concatenation
first_name = "daniel"
last_name = "zadva"
full_name = first_name + " " + last_name
print(full_name) #output: daniel zadva
