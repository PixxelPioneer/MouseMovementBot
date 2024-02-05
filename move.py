import pyautogui
import time
import random

try:
    for z in range(1, 500):
        x = random.randint(0, 500)  # Setting the "X" Axis
        y = random.randint(0, 500)  # Setting the "Y" Axis
        pyautogui.moveTo(x, y)  # Setting the conditions
        

        localtime = time.localtime()  # Capture local time for Logging
        result = time.strftime("%I:%M:%S %p", localtime)  # Format the time

        print('Moved at ' + str(result) + ' (' + str(x) + ', ' + str(y) + ')')  # Print "Moved at" "TIME" "(X,Y)"
        time.sleep(1.4)  # Time to sleep, until next reply

except pyautogui.FailSafeException:
    print("Exit --> Process was interrupted by the User")
    
