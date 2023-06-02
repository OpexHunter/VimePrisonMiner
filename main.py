# pip install pyautogui
# pip install opencv-python
# pip install pillow
from threading import Thread
import math
import time
import numpy as np
from ahk import AHK
import pyautogui
import pytesseract
import keyboard

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
ahk = AHK()
time.sleep(5)

# Pixels Regions
minegreen = ((243, 94, 308), (274, 64, 339))
regbol = (1813, 912, 106, 15)
regcord = (52, 148, 114, 15)
reggr = (267, 185, 141, 16)
blocksee= (1758, 184, 162, 17)
loockatr= (180, 516, 201, 26)

# Funcs
def seeGr():
    gr = str(pytesseract.image_to_string(pyautogui.screenshot(region=reggr)))
    gr = gr.replace(',', '.')
    print(gr)
    x = float(gr[1:gr.find(' ')])
    gr = gr[gr.find(' ') + 1:len(gr)]
    y = float(gr[gr.find(' ') + 1:len(gr) - 2])
    return x, y


def seecords():
    cord = str(pytesseract.image_to_string(pyautogui.screenshot(region=regcord)))
    x = int(cord[0:cord.find(' ')])
    cord = cord[cord.find(' ') + 1:len(cord)]
    y = int(cord[0:cord.find(' ')])
    cord = cord[cord.find(' ') + 1:len(cord)]
    z = int(cord[0:cord.find(' ')])
    return x, y, z


def loockat():
    cord = str(pytesseract.image_to_string(pyautogui.screenshot(region=loockatr)))
    x = int(cord[0:cord.find(' ')])
    cord = cord[cord.find(' ') + 1:len(cord)]
    y = int(cord[0:cord.find(' ')])
    cord = cord[cord.find(' ') + 1:len(cord)]
    z = int(cord[0:cord.find(' ')])
    return x, y, z


def keytime(key, t):
    if len(key) == 1:
        ahk.key_down(key[0])
        time.sleep(t)
        ahk.key_up(key[0])
    if len(key) == 2:
        ahk.key_down(key[0])
        ahk.key_down(key[1])
        time.sleep(t)
        ahk.key_up(key[0])
        ahk.key_up(key[1])


def grad_mouse(x, y):
    for i in range(0, int(abs(x) // 5)):
        ahk.mouse_move(83 * np.sign(x), 0, speed=1, relative=True)
    ahk.mouse_move((16.6 * (x % 5)) // 1, 0, speed=1, relative=True)
    for i in range(0, int(abs(y) // 5)):
        ahk.mouse_move(0, -83 * np.sign(y), speed=1, relative=True)
    ahk.mouse_move(0, -(16.6 * (y % 5)) // 1, speed=1, relative=True)


def mousetoblock(x, z):
    x0,y0,z0=seecords()
    xg,yg=seeGr()
    if (x0 > x) and (z > z0):
        g = math.degrees(math.atan(abs((x0 - x) / (z0 - z))))
        g = g - xg
    elif (x > x0) and (z > z0):
        g = math.degrees(math.atan(abs((z0 - z) / (x0 - x))))
        g = g - xg - 90
    elif (x0 > x) and (z0 > z):
        g = -math.degrees(math.atan(abs((x0 - x) / (z0 - z))))
        g = g - xg + 180
    elif (z0 > z) and (x0 < x):
        g = -math.degrees(math.atan(abs((z0 - z) / (x0 - x))))
        g = g - xg - 90
    grad_mouse(g, 0)


def go_to_block(x, z):
    mousetoblock(x, z)
    ahk.key_down('W')
    while True:
        x0, y0, z0 = seecords()
        if (x0 in range(x - 1, x + 1)) and (z0 in range(z - 1, z + 1)):
            ahk.key_up('W')
            break


def aim():
    while keyboard.is_pressed('esc') == False:
        ahk.key_down('LButton')
        for i in range(2):
            if i == 0:
                ahk.mouse_move(0, 450, speed=1, relative=True)
                ahk.key_up('W')
                keytime('D', 0.5)
                keytime('A', 0.8)
                ahk.key_down('W')
            if i == 1:
                ahk.mouse_move(0, -450, speed=1, relative=True)
                ahk.key_up('W')
                keytime('S', 0.5)
                ahk.key_down('W')
            for i2 in range(4):
                aimblock = pyautogui.locateCenterOnScreen('aim.png', grayscale=True, confidence=0.55,
                                                          region=(0, 540, 1920, 1))
                if aimblock != None:
                    ahk.mouse_move(aimblock[0], ahk.mouse_position[1], speed=1, relative=False)
                    time.sleep(1.5)


def swapitem():
    while keyboard.is_pressed('esc') == False:
        blockname = pytesseract.image_to_string(pyautogui.screenshot(region=blocksee))
        if blockname != '':
            if (blockname.find('log') != -1) or (blockname.find('mel') != -1):
                ahk.key_press('2')
                keytime('Shift', 1)
            else:
                ahk.key_press('1')
                keytime('Shift', 0.5)


# Thread(target=aim).start()
# Thread(target=swapitem).start()

#mousetoblock(249, 242)
#go_to_block(249, 242)

# Debug
'''
Debug = pytesseract.image_to_string(pyautogui.screenshot(region=loockatr))
print(Debug)
'''