#Python3
#autoScroll Script
#@uthor Eishan Jindal
#

import pyautogui,time, sys
#Failsafes are necessary!
pyautogui.FAILSAFE = True

#Pause execution. The user should bring her mouse over to the scrolling window
time.sleep(2)
print("Start")

original = pyautogui.position()
new = original

def termByMouse():
    global original
    global new
    if(new == original):
        return True
    else:
        return False    

while (termByMouse()):
    pyautogui.scroll(-1)
    new = pyautogui.position()
    pyautogui.PAUSE = 4

print("Exit")
