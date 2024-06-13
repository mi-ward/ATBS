import pyautogui, time

time.sleep(5)
pyautogui.click()
distance = 300
change = 20
d = 0
while distance > 0:
    pyautogui.drag(distance,0,duration=d,button='left')
    distance = distance - change
    pyautogui.drag(0, distance, duration=d,button='left')
    pyautogui.drag(-distance, 0, duration=d,button='left')
    distance = distance - change
    pyautogui.drag(0, -distance, duration=d,button='left')
    