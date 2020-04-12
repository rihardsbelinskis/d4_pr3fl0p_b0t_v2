from GotCards import GotCards
from DetectCards import DetectCards
from DetectPosition import DetectPosition
from DetectPrevAction import DetectPrevAction
from PreflopRanges import PreflopRanges
from IsPlayable import IsPlayable
import pyautogui        # not inherited ????


def main():
    im = pyautogui.screenshot(region=(1070, 628, 22, 49))
    im.save(r'card1.png')
    im = pyautogui.screenshot(region=(1162, 628, 22, 49))
    im.save(r'card2.png')

    card1 = ('card1.png')
    card2 = ('card2.png')
    deck = ('deck5.png')
    
    GotCards()
    myHand = DetectCards(card1, card2, deck)
    isPlayable = IsPlayable(myHand)
    print(isPlayable)
    if not isPlayable:
        print("Fold")
    else:
        position = DetectPosition()
        DetectPrevAction(position)
        inRange = PreflopRanges(myHand, position)
        if not inRange:
            print("Fold this hand.")
        else:
            # determine to raise or fold
            print("INSERT Call vs 3bet function here!")



    #i = 2
    #while i>1 :
    #    exec(open('GotCards.py').read())
    #    exec(open('detectcards.py').read())
    #    exec(open('detectprevaction.py').read())
    #    i = 0

if __name__ == "__main__":
    main()
