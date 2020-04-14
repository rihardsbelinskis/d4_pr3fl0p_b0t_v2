import pyautogui
import time

def GotCards():
    
    gotCards = pyautogui.pixel(1070, 628)
    while gotCards[0] == 0:
        time.sleep(1)
        print("...waiting for a hand...")
        gotCards = pyautogui.pixel(1070, 628)
    else:
        gotCards = pyautogui.pixel(1070, 628)
        return gotCards
