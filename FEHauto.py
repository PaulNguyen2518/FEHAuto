# Author: Paul John Nguyen
# Last Updated: 2-12-2019
# Version: 1.0
# Fire Emblem Heroes auto feather farming code via timed mouse clicks.
# Choose your emulator of choice. Just run the python code after adding function calls at the end of this file.

import pyautogui, sys, threading, time, keyboard

done_counting = threading.Event()
	
# function: prints the mouse's current position, use to determine (x, y) coordinates set for autoGHB function
def getMousePosition():
	print(pyautogui.position)
	
	
# function: perform a mouseclick at (x, y) coordinates
# parameter: x = integer
# parameter: y = integer
def mouseClick(x, y):
	pyautogui.click(x, y)
	
	
# function: counts in seconds to inputed paramater "sec", then performs a mouse left click at coordinates (x,y)
# parameter: sec = integer
# parameter: x = integer 
# parameter: y = integer
def count_to(sec, x, y):
	for i in range(1, sec):
		time.sleep(1)
	pyautogui.click(x, y)
	done_counting.set()
		
		
# function: Given a set of arrays that contains integers for seconds, x, y [sec, x, y] (input parameter: secXY),
#			performs the timed clicks in the arrays in sequential order, performs the set k number of times (input paramter: k)
# parameter: secXY = set of arrays
# parameter: k = integer
def autoClick(secXY, k):
	for i in range(1, k+1):
		if(!checkInternet())
			
		actions = secXY[0]
		sec = action1[0]
		x = action1[1]
		y = action1[2]
		thread = threading.Thread(target=count_to(sec, x, y))
		thread.start()
		for j in range(1, len(secXY)):
			actions = secXY[j]
			sec = actions[0]
			x = actions[1]
			y = actions[2]
			thread = threading.Thread(target=count_to(sec, x, y))
		print("Cycle: " + str(i))
	
	
# function: Performs timed clicks in secXY for multiple team in k number of iterations
# parameter: nextTeamClick = array of 3 integers for sec, x, y
# parameter: secXY = set of arrays which have 3 integers for sec, x, y
# parameter: Ks = array of integers for the number of intergers on how many times to iterate for each team
def autoClickMultiTeam(nextTeamClick, secXY, Ks):
	for i in range(0, len(ks)):
		autoClick(sec, Ks[i])
		thread = threading.Thread(target=count_to(nextTeamClick[0], nextTeamClick[1], nextTeamClick[2]))
	
def checkInternet()
	try:
		http.request('GET', 'http://216.58.192.142', retries=False)
		return True
	except urllib3.exceptions.NewConnectionError:
		return False
	
#Sat machias	
#action1 = [7,295,700]
#action2 = [6,286,643]
#action3 = [12,300,300]
#action4 = [7,441,984]
#action5 = [6,290,523]
#action6 = [17,300,300]

#Sun Xander, Mon theguynotinarmor, Tues Narvarre
action1 = [6,295,700]
action2 = [2,286,643]
action3 = [10,466,76]
action4 = [6,441,984]
action5 = [2,290,523]
action6 = [11,300,300]

secXY = [action1,action2,action3,action4,action5,action6]

autoClick(secXY, 130)