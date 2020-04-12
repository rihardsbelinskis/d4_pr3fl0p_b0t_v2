import GotCards
import DetectCards
import DetectPosition
import DetectPrevAction
import PreflopRanges
import pyautogui        # not inherited ????


def main():
    im = pyautogui.screenshot(region=(1070, 628, 22, 49))
    im.save(r'card1.png')
    im = pyautogui.screenshot(region=(1162, 628, 22, 49))
    im.save(r'card2.png')

    card1 = ('card1.png')
    card2 = ('card2.png')
    deck = ('/img/deck5.png')
   
    GotCards(card1, card2, deck)
    if gotCards is None:
        print("No hand dealt yet.")
    else:
        DetectCards(card1, card2, deck)
        IsPlayable(myHand, handMy)
        if isPlayable is None:
            print("Fold this hand.")
        else:
            DetectPosition()
            DetectPrevAction(position)
            PreflopRanges(myHand, handMy, position)
            if inRange is None:
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
