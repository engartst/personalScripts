#!/usr/bin/env python3

import pyautogui
import time
import random

i = 0
j = 0
try:
    while True:
        time.sleep(5)
        if random.random() < 0.5:
            j = -1
        else:
            j = 1
        pyautogui.move(10*random.random()*j, 10*random.random()*j, duration=0.25)
        print(i)
        i+=1
except KeyboardInterrupt:
    print('\nDone.')