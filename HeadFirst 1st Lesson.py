from random import choice

# card = choice(list(deck))
# print(card)
# deck.remove(card)
# print(len(deck))

suits = ["Clubs", "Spades", "Hearts", "Diamond"]
faces = ["Jack", "Queen", "King", "Ace"]

numbers = [_ for _ in range(2, 11)]
deck = set()

for suit in suits : # List comprehension syntax ( result for x in something ...optional conditional ) for creating unique sets of cards 
        [deck.add((card, "of", suit)) for card in (faces + numbers)]

def draw():
    the_card = choice(list(deck))
    deck.remove(the_card)
    return the_card

def check(card=(9, "of", "Hearts")):
      
      if card in deck: 
            print("That card's still in the deck :-)")
      else:
            print("That card's already taken :-(")


x = [(print(draw()), print(f"No. of cards left {len(deck)}"), check()) for _ in  range(5)]