#pyformat output
#using % and .format

#basic formating
name = "Daniel"
age = 35

message = '%s is %d years old' % (name, age)
print(message)

#using format
message = '{} is {} years old.'.format(name, age)
print(message)

#using positional index
message = "{1} year old {0} is doing well.".format(name, age)
print(message)
