from threading import Thread
import time
import numpy as np
from ahk import AHK
import pyautogui
import pytesseract
import keyboard
ahk = AHK()
time.sleep(3)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
reggr=(267,185,141,16)
def go_to_block(x,z):
    mousetoblock(x, z, seecords(), seeGr())
    ahk.key_down('W')
    while True:
        x0, y0, z0 = seecords()
        if (x0 in range(x-1,x+1))and(z0 in range(z-1,z+1)):
            ahk.key_up('W')
            break