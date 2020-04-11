import pyautogui

Player5 = pyautogui.pixel(1525, 466) #SB
if Player5[0] == 102:
    print("SB calls")
elif Player5[0] == 254:
    print("SB raises")
elif Player5[0] == 255:
    print("SB goes ALL IN")
else:
    print("SB folds")

