import pyautogui
import time
from random import choice

comms = ["Reply 1", "Reply 2", "Reply 3", "Reply 4", "Reply 5"]  # array of replies
time.sleep(5)  # time for set up

for i in range(1):  # reply loop
    pyautogui.typewrite(choice(comms))
    pyautogui.typewrite('\n')
    time.sleep(2)