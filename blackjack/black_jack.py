import random

# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# deck = Deck(12)
# print(deck)
# # Should print out:
# # 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# top_card = deck.draw()
# print(top_card)
# print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades

class Card():

    def __init__(self):
        self.color = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.value = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]

class Deck():

    def __init__(self, number):
        self.number = number
        self.card = Card()
        self.number_of_colors = ""
        self.color_counter()

    def draw(self):
        top_card = self.list_of_cards[-2] + " " + self.list_of_cards[-1]
        self.list_of_cards[-1] = ""
        self.list_of_cards[-2] = ""
        self.number -= 1
        self.color_counter()
        return top_card

    def color_counter(self):
        self.list_of_cards = []
        for i in range(self.number//4):
            for color in self.card.color:
                self.list_of_cards.append(random.choice(self.card.value))
                self.list_of_cards.append(color)
        for i in range(self.number%4):
            self.list_of_cards.append(random.choice(self.card.value))
            self.list_of_cards.append( self.card.color[(i-1)+1])
        self.number_of_colors = str(self.number) + " cards - " + str(self.list_of_cards.count("Clubs")) + " Clubs, " + str(self.list_of_cards.count("Diamonds")) + " Diamonds, " + str(self.list_of_cards.count("Hearts")) + " Hearts, " + str(self.list_of_cards.count("Spades")) + " Spades"
        return self.number_of_colors

    def __str__(self):
        return self.number_of_colors

deck = Deck(12)
print(deck)
top_card = deck.draw()
print(top_card)
print(deck)
