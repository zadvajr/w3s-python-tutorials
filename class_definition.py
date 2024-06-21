#class definition in python

class Puppy():

    def __init__(self, name, favorite_toy):
        self.name = name
        self.favorite_toy = favorite_toy
    
    def play(self):
        print(self.name, "is playing with the ", self.favorite_toy)

marble = Puppy('Marble', 'teddy bear')
marble.play() #Marble is playing with the  teddy bear

ornyx = Puppy("Ornyx", "Lizard")
ornyx.play() #Ornyx is playing with the  Lizard