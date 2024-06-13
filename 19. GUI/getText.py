import pyperclip, pyautogui

pyautogui.click(300, 200)
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
text = pyperclip.paste()
print(text)