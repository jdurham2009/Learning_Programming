import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace' ]

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    random.shuffle(deck)
    return deck
create_deck()