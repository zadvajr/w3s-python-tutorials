#python file handling

#write data to file
f = open("myfile.txt", "w")
f.write("This is the first line\n")
f.write("This is the second line\n")
f.close()

#reading from a file
f = open("myfile.txt", "r")
data = f.read()
f.close()
print(data)

#appendind data to a file
f = open("myfile.txt", 'a')
f.write("This is the third line")
f.close
print(data)

#looping through the data file
f = open('myfile.txt', 'r')
for line in f:
    print(line)
f.close()

#writing binary data
import pickle

f = open('pick.dat', 'wb')
pickle.dump(11, f)
pickle.dump('This is a line', f)
pickle.dump([1,2,3,4,5], f)
f.close()

#reading binary data
import pickle
f = open('pick.dat', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()


