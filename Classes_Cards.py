import itertools as it
import random as r


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  # prints card
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        suits = ('\u2660', '\u2663', '\u2665', '\u2666')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                 'Queen', 'King', 'Ace', 'Joker')
        for suit, rank in it.product(suits, ranks):
            self.deck.append(Card(suit, rank))

    def __str__(self):  # prints whole deck
        return 'The deck Is: ' + '\n'.join([str(card) for card in self.deck])

    def shuffle(self):  # shuffles the deck
        r.shuffle(self.deck)

    def get_random(self):  # returns random card from deck
        try:
            return str(r.choice(self.deck))
        except IndexError:
            self.__init__()
            return "No more cards in deck, It was re-created.\nNow you can get random card."

    def pop(self):  # pops card from deck
        try:
            return str(self.deck.pop())
        except IndexError:
            self.__init__()
            return "No more cards in deck, It was re-created.\nNow you can Pop."

    def index(self, value):  # returns card on the inputet index
        if not self.deck:  # if deck is empty
            self.__init__()
            return "No more cards in deck, It was re-created.\nEnter index again."
        try:
            return str(self.deck[int(value)])
        except IndexError:
            return "Your index is out of range."
        except ValueError:
            return "Index should be a number."

