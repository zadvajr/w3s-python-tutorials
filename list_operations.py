#list operations

mylist = [1,2,3,4,5]

#prints the maximum number in mylist
print(max(mylist))

#prints the minimum number in mylist
print(min(mylist))

#prints the sum of elements in mylist
print(sum(mylist))

#prints the length of mylist
print(len(mylist))

#checks if 6 in mylist 
print(6 in mylist)

#checks if 6 is not in mylist
print(6 not in mylist)

# + and * effect on list
list1 = [1,2,3]
list2 = [4,5,6]


#using + to join lists
list3 = list1 + list2
print(list3) #prints [1,2,3,4,5,6]

#using * to replicate lists
print(list1 * 3)

#append element to list
list1.append(4)
print(list1)

#count the number of times elements appears in a list
print(list1.count(1))

#extend list
list1.extend(list2)
print(list1)

