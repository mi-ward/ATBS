1. How can you trigger PyAutoGUI’s fail-safe to stop a program?
    - ctrl -c or drag to one of the corners of the screen

2. What function returns the current resolution()?
    - pyautogui.size()

3. What function returns the coordinates for the mouse cursor’s current position?
    - pyautogui.position()

4. What is the difference between pyautogui.moveTo() and pyautogui.move()?
    - pyautogui.move() moves the cursor relative to the current position. pyautogui.moveTo() moves the cursor relevant to the screen

5. What functions can be used to drag the mouse?
    - pyautogui.drag() and pyautogui.dragTo()

6. What function call will type out the characters of "Hello, world!"?
    - pyautogui.write("Hello, world!")

7. How can you do keypresses for special keys such as the keyboard’s left arrow key?
    - type them in with the special name, "arrow", you can use pyautogui.write() or pyautogui.press()

8. How can you save the current contents of the screen to an image file named screenshot.png?
    - pyautogui.screenshot('screenshot.png')


9. What code would set a two-second pause after every PyAutoGUI function call?
    - pyautogui.PAUSE = 2

10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?
    - Selenium

11. What makes PyAutoGUI error-prone?
    - it's dumb and does actions blindly.

12. How can you find the size of every window on the screen that includes the text Notepad in its title?
    pyautogui.getWindowsWithTitle('Notepad')

13. How can you make, say, the Firefox browser active and in front of every other window on the screen?
    - pyautogui.getWindowsWithTitle('Firefox') 
      then w.activate()