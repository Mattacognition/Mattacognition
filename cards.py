import random
# Deck of Cards

class Card:
    suits = ['D', 'H', 'C', 'S']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    drawn = []
    card = ""
    hand = []


    def dealCard(suits, numbers, drawn, hand):
        suit = suits[random.randint(0, len(suits) - 1)]
        number = numbers[random.randint(0, len(numbers) - 1)]
        card = number + suit
        print(card)
        hand.append(card)
        drawn.append(card)

        return card
    
    def dealHand(card, suits, numbers, drawn, hand, dealCard):
        while len(hand) < 5:
            if card not in drawn:
                dealCard(suits, numbers, drawn, hand)
            else:
                print("duplicate")






    dealHand(card, suits, numbers, drawn, hand, dealCard)

    print('hand', hand)

    print('drawn', drawn)


















    # diamonds = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD']
    # hearts =  ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH']
    # clubs = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC']
    # spades = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']

# class Deck:
#     deck = [diamonds, hearts, clubs, spades]

# suit = deck[random.randint(0, len(deck) - 1)]


# print(suit)