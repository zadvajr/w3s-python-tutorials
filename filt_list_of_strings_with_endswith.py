some_text = ["boys", "girls", "male", "female"]
with_s = []
without_s = []

for word in some_text:
    if(word.endswith('s')):
        with_s.append(word)
    else:
        without_s.append(word)

print(with_s)
print(without_s)