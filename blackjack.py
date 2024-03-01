from cards import Card

def blackjack():    
    hands = Card.dealHand(card=Card.card, suits=Card.suits, numbers=Card.numbers, drawn=Card.drawn, hand=Card.hand, handSize=2, dealCard=Card.dealCard)
    # print("here", hands)
    blackjackHand = Card.hand
    print(blackjackHand)
    return blackjackHand
blackjack()