import pyautogui
import mouse
import keyboard
from time import sleep


while True:
	f = open('text.txt', 'w')

    events = []                 
    mouse.hook(events.append)   #record
    keyboard.wait("a")   # whait button "a" and stop record       
    mouse.unhook(events.append) #Stop record

    for i in range(0,len(events)):
    	f.write(str(events[i]))

    f.close()
