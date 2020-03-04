import random as r
import itertools as it


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  # prints card
        return self.rank + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        suits = ('\u2660', '\u2663', '\u2665', '\u2666')
        ranks = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
        for suit, rank in it.product(suits, ranks):
            self.deck.append(Card(suit, rank))

    def shuffle(self):
        r.shuffle(self.deck)

    def __str__(self):
        return 'Your Deck: ' + (" ".join([str(card) for card in self.deck]))

    def get_random(self):
        try:
            return str(r.choice(self.deck))
        except IndexError:
            self.__init__()
            return "Howdy! Deck is empty, it was organize again"

    def pop(self):
        try:
            return str(self.deck.pop())
        except IndexError:
            self.__init__()
            return "Howdy! Deck is empty, it was organize again"

    def index(self, value):
        if not self.deck:
            self.__init__()
            return "Howdy! Deck is empty, it was organize again"
        try:
            return str(self.deck[int(value)])
        except IndexError:
            return "Your index is out of range."
        except ValueError:
            return "Index should be a number."
