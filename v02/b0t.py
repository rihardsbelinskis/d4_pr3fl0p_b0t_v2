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
    deck = ('deck5.png')
    
    #i = 2
    #while i>1 :
    #    exec(open('GotCards.py').read())
    #    exec(open('detectcards.py').read())
    #    exec(open('detectprevaction.py').read())
    #    i = 0

if __name__ == "__main__":
    main()
