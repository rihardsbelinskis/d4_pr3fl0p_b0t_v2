from GotCards import *
from DetectCards import *
from DetectPosition import *
from DetectPrevAction import *
from PreflopRanges import *
from IsPlayable import *

def main():

    im = pyautogui.screenshot(region=(1070, 628, 22, 49))
    im.save(r'card1.png')
    im = pyautogui.screenshot(region=(1162, 628, 22, 49))
    im.save(r'card2.png')

    card1 = ('card1.png')
    card2 = ('card2.png')
    deck = ('../img/Deck5.png')
    
    GotCards()
    myHand = DetectCards(card1, card2, deck)
    isPlayable = IsPlayable(myHand)
    if not isPlayable:
        print("Hand is unplayable. Fold.")
    else:
        position = DetectPosition()
        DetectPrevAction(position)
        inRange = PreflopRanges(myHand, position)
        if not inRange:
            print("Hand not in range. Fold.")
        else:
            # determine to raise or fold
            print("INSERT Call vs 3bet function here!")

if __name__ == "__main__":
    
    main()
