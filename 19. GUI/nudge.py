import pyautogui, time

while True:
    pyautogui.move(0, 1)
    pyautogui.move(1, 0)
    pyautogui.move(0, -1)
    pyautogui.move(-1, 0)
    time.sleep(10)
    