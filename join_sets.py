#join sets

#join sets with union() method
# union method joins two sets and return a new set containing elements from both of the sets

set1 = {'00', '01', '02', '03', '04'}
set2 = {'05', '06', '07', '08'}

set3 = set1.union(set2)

print(set3)

#end union()

#update() to join sets
# you can also use update method to join two sets however, it doesn't return a new set as in union

set4 = {1, 2, 3, 4, 5, 6}

set4.update(set2)

print(set4)

#end update()

#intersection_update() 
# keeps only the duplicate

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) #prints {"apple"}

# end intersection_update()

#intersection() this unlike intersection_update() returns a new set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "banana"}

z = x.intersection(y)

print(z) 

#end intersection()

#sysmetric_difference_update() keeps all but duplicates it updates the existing set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "banana"}

x.symmetric_difference_update(y)

print(x)

#end

#symetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "banana"}

z = x.symmetric_difference(y)

print(z)

#end

