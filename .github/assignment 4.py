# Programmers: Victoria Shelton
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

import random

deck = []
point = 0
cards = []

# Function that creates a deck of cards and chooses a random card
def shuffle_deck(num_card):
    # initialize lists and counter
    x = 1
    hearts = []
    diamonds = []
    spades = []
    clubs = []
    # Adds number cards
    while x <= 13:
        hearts.append("H" + str(x))
        diamonds.append("D" + str(x))
        spades.append("S" + str(x))
        clubs.append("C" + str(x))
        x += 1
    # combines lists into one list
    cards = hearts + diamonds + spades + clubs
    # randomizes/shuffles cards
    random.shuffle(cards)
    return cards[1:num_card]


# This function converts the name of a card if it is an Ace, Jack, Queen, or King
def convert(card):
    name_card = card
    if "1" in card:
        if "H" in card:
            name_card = "Ace of Hearts"
        if "D" in card:
            name_card = "Ace of Diamonds"
        if "S" in card:
            name_card = "Ace of Spades"
        if "C" in card:
            name_card = "Ace of Clubs"
    elif "11" in card:
        if "H" in card:
            name_card = "Jack of Hearts"
        if "D" in card:
            name_card = "Jack of Diamonds"
        if "S" in card:
            name_card = "Jack of Spades"
        if "C" in card:
            name_card = "Jack of Clubs"
    elif "12" in card:
        if "H" in card:
            name_card = "Queen of Hearts"
        if "D" in card:
            name_card = "Queen of Diamonds"
        if "S" in card:
            name_card = "Queen of Spades"
        if "C" in card:
            name_card = "Queen of Clubs"
    elif "13" in card:
        if "H" in card:
            name_card = "King of Hearts"
        if "D" in card:
            name_card = "King of Diamonds"
        if "S" in card:
            name_card = "King of Spades"
        if "C" in card:
            name_card = "King of Clubs"
    else:
        if "H" in card:
            name_card = card[1] + " of Hearts"
        if "D" in card:
            name_card = card[1] + " of Diamonds"
        if "S" in card:
            name_card = card[1] + " of Spades"
        if "C" in card:
            name_card = card[1] + " of Clubs"
    return name_card


# This function determines the values of the cards
def value_of_card(card):
    if "11" in card:
        value = 10
    elif "12" in card:
        value = 10
    elif "13" in card:
        value = 10
    elif "1" in card:
        value = 11
    else:
        value = card[1:3]
    value = int(value)
    return value


# This function creates the starting deck of two cards
def hand():
    deck.append(shuffle_deck(2))
    print("You have these cards: ", convert(deck[0]), ",", convert(deck[0]))


# this function adds a card
def add_card():
    x = 0
    deck.append(shuffle_deck(1))
    for i in deck:
        print(convert(deck[x]))
        x += 1


# Adds the values of the cards in the deck
def points():
    global point
    x = 0
    for i in deck:
        point += value_of_card(deck[x])
        x += 1
    print("The total value of your cards is:", point)


def play():
    hand()
    points()
    hit = True
    while hit:
        choice = input("Would you like to draw another card? (y/n) ")
        choice = choice.strip()
        if choice == "y":
            add_card()
            points()
        else:
            hit = False
            if point == 21:
                print("You win!")


def main():
    play()


main()
