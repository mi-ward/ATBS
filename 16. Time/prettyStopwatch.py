#! python3
#stopwatch.py - A simple stopwatch program.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.' \
      'Press CTRL-C to quit.')

input()  
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
pyperclip.copy("")

# Start tracking the lap times.
try:
    while True:
        clipboard = pyperclip.paste()
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapNum_rjust = str(lapNum).rjust(2)
        totalTime_rjust = str(totalTime).rjust(5)
        lapTime_rjust = str(lapTime).rjust(5)
        text = "Lap #%s: %s (%s)" % (lapNum_rjust, totalTime_rjust, lapTime_rjust)
        clipboard += (text + '\n')
        pyperclip.copy(clipboard)
        print(text, end='')
        
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the CTRL-C exception to keep its error message from displaying.
    print('\nDone.')