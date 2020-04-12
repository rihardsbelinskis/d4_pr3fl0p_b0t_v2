import pytesseract
import pyautogui
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 3 --psm 6 outputbase digits'

#NAUDA PIE GALDIEM
                                                                    #TE BUS PROBLEMAS

player1 = pyautogui.screenshot(region=(670, 742, 147, 33))
image1 = np.array(player1)
image1 = image1[:, :, ::-1].copy()
img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(img1,50,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Black and white', thresh1)
money1 = pytesseract.image_to_string(thresh1, config = custom_config)
print(r'Player 1:',money1)

player2 = pyautogui.screenshot(region=(332, 429, 147, 33))
image2 = np.array(player2)
image2 = image2[:, :, ::-1].copy()
img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(img2,50,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Black and white', thresh2)
money2 = pytesseract.image_to_string(thresh2, config = custom_config)
print(r'Player 2:',money2)

player3 = pyautogui.screenshot(region=(670, 148, 147, 33))
image3 = np.array(player3)
image3 = image3[:, :, ::-1].copy()
img3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
ret,thresh3 = cv2.threshold(img3,50,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Black and white', thresh3)
money3 = pytesseract.image_to_string(thresh3, config = custom_config)
print(r'Player 3:',money3)

player4 = pyautogui.screenshot(region=(1110, 148, 147, 33))
image4 = np.array(player4)
image4 = image4[:, :, ::-1].copy()
img4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
ret,thresh4 = cv2.threshold(img4,50,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Black and white', thresh4)
money4 = pytesseract.image_to_string(thresh4, config = custom_config)
print(r'Player 4:',money4)

player5 = pyautogui.screenshot(region=(1473, 431, 147, 33))
image5 = np.array(player5)
image5 = image5[:, :, ::-1].copy()
img5 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
ret,thresh5 = cv2.threshold(img5,50,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Black and white', thresh5)
money5 = pytesseract.image_to_string(thresh5, config = custom_config)
print(r'Player 5:',money5)

player6 = pyautogui.screenshot(region=(1110, 742, 147, 33))
image6 = np.array(player6)
image6 = image6[:, :, ::-1].copy()
img6 = cv2.cvtColor(image6, cv2.COLOR_BGR2GRAY)
ret,thresh6 = cv2.threshold(img6,50,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Black and white', thresh6)
money6 = pytesseract.image_to_string(thresh6, config = custom_config)
print(r'Player 6:',money6)
