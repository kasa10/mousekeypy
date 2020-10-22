import pyautogui
import mouse
from time import sleep



while True:
	if mouse.is_pressed(button='left'):
		print(pyautogui.position())
		sleep(1)

		