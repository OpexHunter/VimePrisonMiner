import pytesseract
from PIL import Image
import pyautogui
import time
time.sleep(3)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pyautogui.screenshot('seeMe.png',region=(0,180,480,320))
img=Image.open('seeMe.png')

text = pytesseract.image_to_string(img, lang='eng')
print(text)