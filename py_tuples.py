#python tuples
#creating tuple
t1 = ()
print(t1)
print(type(t1))

#tuple with single element
t2 = (2,)
print(t2)

#tuples from list
t4 = tuple([1,2,3,4])
print(t4)
print(type(t4))

#tuple from string
t5 = tuple("abcd")
print(t5)
print(type(t5))

#tuples functions max(), min(), len() and sum
mytuple = (1,2,3,4,5,6)
print(max(mytuple))
print(min(mytuple))
print(len(mytuple))
print(sum(mytuple))

#iterating through tuple
for i in mytuple:
    print(i, end=" ")

