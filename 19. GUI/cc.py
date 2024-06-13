import time, pyautogui

time.sleep(1)
pyautogui.PAUSE = 0

i = 0
while i < 1:
    pyautogui.moveTo(800,400)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    
    i += 1
    print(i)