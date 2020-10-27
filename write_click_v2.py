import pyautogui
import mouse
import keyboard
from time import sleep


events = []  

while True:
    if mouse.is_pressed(button='left'):
        events.append(pyautogui.position())
        sleep(1)
    




    if keyboard.is_pressed('z'):
        f = open('click.txt', 'w')

        for i in range(0,len(events)):
            f.write('pyautogui.click('+str(events[i][0])+', '+str(events[i][1])+')\n')

        f.close()

        sys.exit()



