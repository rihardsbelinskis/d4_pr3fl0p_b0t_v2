from DetectPosition import *
import time

# THINK ABOUT ADDING "prevAction" variable, which determines what to do post-flop as well
    
def DetectPrevAction(position):

    # CHECK IF THE ACTION IS ON ME
    checkBTN = (1, 1, 1)
    while checkBTN[0] >  0:
        checkBTN = pyautogui.pixel(880, 890)
    print("Action is on me!")
    time.sleep(3.1)

    # CHECK THE ACTION BEFORE ME
    Player1 = pyautogui.pixel(720, 779)
    Player2 = pyautogui.pixel(395, 466)
    Player3 = pyautogui.pixel(720, 183)
    Player4 = pyautogui.pixel(1152, 183)
    Player5 = pyautogui.pixel(1525, 466)

    # COLOR CODING FOR ACTION PLATES
    # 5 ir folds (zils)
    # 254 ir raise (oranzs)
    # 255 ir allin (sarkans)
    # 102 ir check/call (zals)

    if position == "MP": 
        #UTG
        if Player5[0] == 102:
            print("UTG calls")
        elif Player5[0] == 254:
            print("UTG raises")
        elif Player5[0] == 255:
            print("UTG goes ALL IN")
        else:
            print("UTG folds")

    if position == "CO":
        #UTG
        if Player4[0] == 102:
            print("UTG calls")
        elif Player4[0] == 254:
            print("UTG raises")
        elif Player4[0] == 255:
            print("UTG goes ALL IN")
        else:
            print("UTG folds")
        #MP
        if Player5[0] == 102:
            print("MP calls")
        elif Player5[0] == 254:
            print("MP raises")
        elif Player5[0] == 255:
            print("MP goes ALL IN")
        else:
            print("MP folds")
            
    if position == "BTN":
        #UTG
        if Player3[0] == 102:
            print("UTG calls")
        elif Player3[0] == 254:
            print("UTG raises")
        elif Player3[0] == 255:
            print("UTG goes ALL IN")
        else:
            print("UTG folds")
        #MP
        if Player4[0] == 102:
            print("MP calls")
        elif Player4[0] == 254:
            print("MP raises")
        elif Player4[0] == 255:
            print("MP goes ALL IN")
        else:
            print("MP folds")
        #CO
        if Player5[0] == 102:
            print("CO calls")
        elif Player5[0] == 254:
            print("CO raises")
        elif Player5[0] == 255:
            print("CO goes ALL IN")
        else:
            print("CO folds")

    if position == "SB": 
        #UTG
        if Player2[0] == 102:
            print("UTG calls")
        elif Player2[0] == 254:
            print("UTG raises")
        elif Player2[0] == 255:
            print("UTG goes ALL IN")
        else:
            print("UTG folds")
        #MP
        if Player3[0] == 102:
            print("MP calls")
        elif Player3[0] == 254:
            print("MP raises")
        elif Player3[0] == 255:
            print("MP goes ALL IN")
        else:
            print("MP folds")
        #CO
        if Player4[0] == 102:
            print("CO calls")
        elif Player4[0] == 254:
            print("CO raises")
        elif Player4[0] == 255:
            print("CO goes ALL IN")
        else:
            print("CO folds")
        #BTN
        if Player5[0] == 102:
            print("BTN calls")
        elif Player5[0] == 254:
            print("BTN raises")
        elif Player5[0] == 255:
            print("BTN goes ALL IN")
        else:
            print("BTN folds")

    if position == "BB": 
        #UTG
        if Player1[0] == 102:
            print("UTG calls")
        elif Player1[0] == 254:
            print("UTG raises")
        elif Player1[0] == 255:
            print("UTG goes ALL IN")
        else:
            print("UTG folds")
        #MP
        if Player2[0] == 102:
            print("MP calls")
        elif Player2[0] == 254:
            print("MP raises")
        elif Player2[0] == 255:
            print("MP goes ALL IN")
        else:
            print("MP folds")
        #CO
        if Player3[0] == 102:
            print("CO calls")
        elif Player3[0] == 254:
            print("CO raises")
        elif Player3[0] == 255:
            print("CO goes ALL IN")
        else:
            print("CO folds")
        #BTN
        if Player4[0] == 102:
            print("BTN calls")
        elif Player4[0] == 254:
            print("BTN raises")
        elif Player4[0] == 255:
            print("BTN goes ALL IN")
        else:
            print("BTN folds")
        #SB
        if Player5[0] == 102:
            print("SB calls")
        elif Player5[0] == 254:
            print("SB raises")
        elif Player5[0] == 255:
            print("SB goes ALL IN")
        else:
            print("SB folds")
