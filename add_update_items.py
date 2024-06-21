#adding items to set
#once a set is created you cannot change items but you can add items to it

topideas = {"tech", "agro", "retail"}

print(topideas)

topideas.add("health")

print(topideas) #{'health', 'retail', 'agro', 'tech'} adds it to beginninng

#adding another set to set

subideas = {"Printing", "Digital printing"}

topideas.update(subideas)

print(topideas) # {'retail', 'health', 'agro', 'Digital printing', 'Printing', 'tech'}

#you can as well add any iterable like list to set

bestideas = ["AI", "Robotics"]

topideas.update(bestideas)

print(topideas) #{'Robotics', 'retail', 'agro', 'Digital printing', 'health', 'AI', 'tech', 'Printing'}

# remove items in set
# there are two ways to remove an item in a set 1. remove() and 2. discard()


topideas.remove("AI")

print(topideas) #{'health', 'agro', 'retail', 'tech', 'Robotics', 'Printing', 'Digital printing'}

topideas.discard("Digital printing")

print(topideas) #{'retail', 'tech', 'Robotics', 'health', 'Printing', 'agro'}


#loop through set

for i in topideas:
    print(i)