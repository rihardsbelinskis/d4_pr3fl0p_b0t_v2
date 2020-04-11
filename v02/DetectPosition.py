import pyautogui    # this should be discluded after IsPlayable is ready
import IsPlayable  

def DetectPosition():
    if isPosition = True:
        dealerBTN1 = pyautogui.pixel(1284, 596)
        dealerBTN2 = pyautogui.pixel(840, 596)
        dealerBTN3 = pyautogui.pixel(563, 360)
        dealerBTN4 = pyautogui.pixel(840, 222)
        dealerBTN5 = pyautogui.pixel(1284, 222)
        dealerBTN6 = pyautogui.pixel(1356, 360)

        if dealerBTN1[0] == 5:
            position = ("BTN")
        elif dealerBTN2[0] == 5:
            position = ("CO")
        elif dealerBTN3[0] == 5:
            position = ("MP")
        elif dealerBTN4[0] == 5:
            position = ("UTG")
        elif dealerBTN5[0] == 5:
            position = ("BB")
        else:
            position = ("SB")

        print(f'Hero is in {position}')

    else:
        # call the "fold function"
        
    return position
