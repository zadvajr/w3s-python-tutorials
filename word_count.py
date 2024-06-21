#word count
#this python scripts accepts a text file name 
#loops through the lines in the file and count each words occurence and prints out the 
# word with the highest count

file_name = input("Enter Text File Name: ") #prompts file name
file_handle = open(file_name) #opens the file

word_counts = dict() #empty dictionary to store words count

for line in file_handle:
    words = line.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) +1
    
bigcount = None
bigword = None

for word, word_counts in word_counts.items():
    if bigcount is None or word_counts > bigcount:
        bigword = word
        bigcount = word_counts

print(bigword, bigcount)