import pyautogui as pg
import time

time.sleep(10)
file = open("spam.txt", "r")
for word in file:
    pg.typewrite(word)
pg.press("enter")