import pyautogui
import time
gotCards = pyautogui.pixel(1070, 628)

while gotCards[0] == 0:
    time.sleep(1)
    print("Nav karshu vel")
    gotCards = pyautogui.pixel(1070, 628)
else:
    print("man ir hands")
