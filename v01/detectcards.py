import pyautogui
import time
#s=pyautogui.screenshot()
#a = s.getpixel((640, 350, 0)) #atrod konkreta piksela rgb datus


#s.save(r'screen.png')



# atrod visas vietas, kur uz ekrana atrodas bilde nba.png un uzraksta
# koordinates katrai bildei
#i = 0
#for pos in pyautogui.locateAllOnScreen('BOT1table.png'):
#    i= i+1
#print("there are ", i, "tables")

####### NOSAKA, CIK GALDI IR ATVERTI PEC PISKELA STARP GALDIEM ###########
##########################################################################
#pix6 = pyautogui.pixel(640, 350)
#pix4 = pyautogui.pixel(700, 350)
#pix2 = pyautogui.pixel(960, 350)

#if (pix6[0]) == 3 :
#    print("ir 6 galdi!")
#elif (pix4[0]) == 3:
#    print('ir 4 galdi!')
#elif (pix2[0]) == 3:
#    print('ir 2 galdi!')
#else:
#    print('ir 1 galds!')
###########################################################################
###########################################################################



###############SALIDZINA KARTS SCRENSHOTU AR DECKU###############################
im = pyautogui.screenshot(region=(1070, 628, 22, 49))
im.save(r'karts1.png')
im = pyautogui.screenshot(region=(1162, 628, 22, 49))
im.save(r'karts2.png')
karts1 = ('karts1.png')
karts2 = ('karts2.png')
deck = ('deck5.png')
card1 = pyautogui.locate(karts1, deck, grayscale=False)
Value1 = card1[0]
Suit1 = card1[1]
#print(Suit1, Value1)
card2 = pyautogui.locate(karts2, deck, grayscale=False)
Value2 = card2[0]
Suit2 = card2[1]
#print(Suit2, Value2)

#nosaka karts1 vertibu
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
elif Value1 == 3511:
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

#nosaka karts1 suitu
if Suit1 == 1:
    CardSuit1 = "s"
elif Suit1 == 99:
    CardSuit1 = "c"
elif Suit1 == 197:
    CardSuit1 = "d"
elif Suit1 == 295:
    CardSuit1 = "h"


#nosaka karts2 vertibu
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
elif Value2 == 3511:
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

#nosaka karts2 suitu
if Suit2 == 1:
    CardSuit2 = "s"
elif Suit2 == 99:
    CardSuit2 = "c"
elif Suit2 == 197:
    CardSuit2 = "d"
elif Suit2 == 295:
    CardSuit2 = "h"

#print(f'My first card is {CardValue1}{CardSuit1}')
#print(f'My second card is {CardValue2}{CardSuit2}')
if CardSuit1 == CardSuit2:
    Suit = "s"
else:
    Suit = "o"
print(f'My hand is: {CardValue1}{CardValue2}{Suit}')
################################################################################

