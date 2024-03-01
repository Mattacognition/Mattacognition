from cards import Card

def poker():    
    hands = Card.dealHand(card=Card.card, suits=Card.suits, numbers=Card.numbers, drawn=Card.drawn, hand=Card.hand, handSize=5, dealCard=Card.dealCard)
    # print("here", hands)
    pokerHand = Card.hand
    print(pokerHand)
    return pokerHand
poker()
# print("handy", hands)