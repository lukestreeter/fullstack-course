def __init__(self):
print("Creating New Ordered Deck!")
self.allcards = [(s,r) for s SUITE for r in RANKS]

def shuffle(self):
print("SHUFFLING DECK")
shuffle(self.allcards):

def split_in_half(self):
    return (self.allcards[:26],self.allcards[26:])

    def __init__(self,cards):
self.cards = cards

def __str__(self):
return "Contains {} cards".format(len(self.cards))

def add(self,added_cards):
self.cards.extend(added_cards)

def remove_card(self):
return self.cards.pop()

def __init__(self,name,hand):
self.name = name 
self.hand = hand

def play_card(self):
drawn_card = self.hand.remove_card():
print("{} has placed: {}".format(self.name,drawn_card))
print("/n")
return drawn_card

def remove_war_cards(self):
war_cards = []
for x in range(3):
war_cards.append(self.hand.remove_card()):
return war_cards

def still_has_cards(self):
"""
Return True if player still has cards left
"""
return len(self.hand.cards) != 0

print("Welcome to War, let's begin...")

# Create new deck and split it in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# create both players!
comp = Player("computer",Hand(half1))

name = input("what is your name?")
user = Player(name,Hand(half2))

total_rounds = 0 
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
total_rounds += 1
print("Time for a new round!")
print("here are  the current standings")
print(comp.name+"has the count:"+str(len(comp.hand.cards)))























