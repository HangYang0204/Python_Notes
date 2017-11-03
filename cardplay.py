import random
#encode
#see example of defination of variables in a class, which is called class
#attribute, and are accessed with dot notation. Comparing it with the instabce
#attribute
class Card(object):
    #def variables
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack',
    'Queen','King']
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    #__init__
    def __init__(self,suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
    #__str__:object attribute is called by object while instance attribute is called
    #by instance. Comparing Card. and self. in below example
    def __str__(self):
        return '%s of %s' %(Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __lt__(self, other):
        #Suit is more important
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return 1
        #if suit are the same,compare rank
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0

card1 = Card(1,12)
card2 = Card(2,2)

##print(card1.__lt__(card2))
#define Deck object
class Deck(object):
    """a collection of cards"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
##print(deck)
deck.shuffle()

print(deck)






