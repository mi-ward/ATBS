import pyautogui, time
mouseBuffer = 20

print('Set up page now.')
time.sleep(5)
chatters = ['john@example.com']

for chatter in chatters:
    startChatCoords = pyautogui.locateOnScreen('startChat.png')
    pyautogui.click(startChatCoords[0] + mouseBuffer, startChatCoords[1] + mouseBuffer)
    time.sleep(0.5)
    pyautogui.write(chatter)
    time.sleep(2)
    pyautogui.press(['enter', 'enter'])
    time.sleep(3)
    pyautogui.write('Follow the white rabbit...')
    pyautogui.press('enter')
    backArrowCoords = pyautogui.locateOnScreen('backArrow.png')
    pyautogui.click(backArrowCoords[0] + mouseBuffer, backArrowCoords[1] + mouseBuffer)
    time.sleep(3)

print('Done')