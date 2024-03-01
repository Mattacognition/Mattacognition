import random
# Deck of Cards

class Card:
    suits = ['D', 'H', 'C', 'S']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    drawn = []
    card = ""
    hand = []
    handSize = 5

    def dealCard(suits, numbers, drawn, hand):
        suit = suits[random.randint(0, len(suits) - 1)]
        number = numbers[random.randint(0, len(numbers) - 1)]
        card = number + suit
        # print(card)
        if card not in drawn:
            hand.append(card)
            drawn.append(card)

        return card
    
    def dealHand(card, suits, numbers, drawn, hand, handSize, dealCard):
        while len(hand) < handSize:
            dealCard(suits, numbers, drawn, hand)

    # dealHand(card, suits, numbers, drawn, hand, handSize, dealCard)

    # print('hand', hand)
    
# hand = Card.dealHand()
# print(hand)

    # print('drawn', drawn)
