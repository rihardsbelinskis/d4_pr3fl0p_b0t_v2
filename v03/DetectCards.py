from GotCards import *

def DetectCards(card1, card2, deck):
    
    myHand = []
    
    card1_pos = pyautogui.locate(card1, deck, grayscale=False)
    Value1 = card1_pos[0]
    Suit1 = card1_pos[1]
    
    card2_pos = pyautogui.locate(card2, deck, grayscale=False)
    Value2 = card2_pos[0]
    Suit2 = card2_pos[1]

    #Value of card 1
    if Value1 == 1:
        CardValue1 = "2"
    elif Value1 == 71:
        CardValue1 = "3"
    elif Value1 == 141:
        CardValue1 = "4"
    elif Value1 == 211:
        CardValue1 = "5"
    elif Value1 == 281:
        CardValue1 = "6"
    elif Value1 == 351:
        CardValue1 = "7"
    elif Value1 == 421:
        CardValue1 = "8"
    elif Value1 == 491:
        CardValue1 = "9"
    elif Value1 == 561:
        CardValue1 = "T"
    elif Value1 == 631:
        CardValue1 = "J"
    elif Value1 == 701:
        CardValue1 = "Q"
    elif Value1 == 771:
        CardValue1 = "K"
    elif Value1 == 841:
        CardValue1 = "A"
    else:
        print("Error. Value of card 1 undetected!")

    #Suit of card 1
    if Suit1 == 1:
        CardSuit1 = "s"
    elif Suit1 == 99:
        CardSuit1 = "c"
    elif Suit1 == 197:
        CardSuit1 = "d"
    elif Suit1 == 295:
        CardSuit1 = "h"
    else:
        print("Error. Suit of card 1 undetected!")

    #Value of card 2
    if Value2 == 1:
        CardValue2 = "2"
    elif Value2 == 71:
        CardValue2 = "3"
    elif Value2 == 141:
        CardValue2 = "4"
    elif Value2 == 211:
        CardValue2 = "5"
    elif Value2 == 281:
        CardValue2 = "6"
    elif Value2 == 351:
        CardValue2 = "7"
    elif Value2 == 421:
        CardValue2 = "8"
    elif Value2 == 491:
        CardValue2 = "9"
    elif Value2 == 561:
        CardValue2 = "T"
    elif Value2 == 631:
        CardValue2 = "J"
    elif Value2 == 701:
        CardValue2 = "Q"
    elif Value2 == 771:
        CardValue2 = "K"
    elif Value2 == 841:
        CardValue2 = "A"
    else:
        print("Error. Value of card 2 undetected!")

    #Suit of card 2
    if Suit2 == 1:
        CardSuit2 = "s"
    elif Suit2 == 99:
        CardSuit2 = "c"
    elif Suit2 == 197:
        CardSuit2 = "d"
    elif Suit2 == 295:
        CardSuit2 = "h"
    else:
        print("Error. Suit of card 2 undetected!")

    if CardSuit1 == CardSuit2:
        Suit = "s"
    else:
        Suit = "o"
    

    myHand = CardValue1+CardValue2+Suit
    print(f'Dealt to Hero: {myHand}')

    return(myHand)
