import pyautogui
import time

####### NOSAKA, CIK GALDI IR ATVERTI PEC PISKELA STARP GALDIEM ###########
##########################################################################
#! ! ! I M P O R T A N T ! ! !
# jaizmanto ekranam bilde ar solid krasu rgb(3, 131, 135)
pix6 = pyautogui.pixel(640, 350)
pix4 = pyautogui.pixel(700, 350)
pix2 = pyautogui.pixel(960, 350)

if (pix6[0]) == 3 :
    print("ir 6 galdi!")
elif (pix4[0]) == 3:
    print('ir 4 galdi!')
elif (pix2[0]) == 3:
    print('ir 2 galdi!')
else:
    print('ir 1 galds!')
###########################################################################
###########################################################################
print("Izprinteju sho pirms atradishu kartis")
