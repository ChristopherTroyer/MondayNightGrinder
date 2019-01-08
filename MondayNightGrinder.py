import pyautogui
import time
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

x = 0

while(True):
	print("Clicking start game")
	pyautogui.click(x=1230, y=583)
	time.sleep(17)
	print("Picking assassin")
	pyautogui.click(x=1023, y=626)
	time.sleep(.7)
	print("Locking in")
	pyautogui.click(x=760, y=866)
	print("waiting for intro")
	time.sleep(23)
	print("intro over, now spamming")
	for x in range (33):
		pyautogui.click()
		print("seconds past: ", x)
		time.sleep(1)
	print("game over")
	time.sleep(4)
	x + 1
	if(x >= 10):
		print("taking screenshot")
		img1 = pyautogui.screenshot("MondayNightLevel.png", region=(352,569,576,165))
		x = 0
	pyautogui.click(x=1495, y=897)
	print("start over")
	time.sleep(3)