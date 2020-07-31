# James Cox
# 6-20-2020

"""
This is a single player battleship game.
The ships will be randomly placed, and the user will try to find them all.

create a function to randomly place the ships and return a grid to store
Create two lists, one for the ships, and one for the board.
create a function to print a pretty version of the board, O's for guesses and X's for hits
Implement gameplay
	keep a total of hits and add 1 to each hit.  end game when the total ='s the total available hits

"""

import random
#This function will take an input of a list and print each item to the console.
def printList(inputList):
	for i in inputList:
		print(str(i))

#this function returns a grid of the placed shapes
def placeShips():
	retGrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
	# ships to be placed randomly in the grid
	ships = [2, 3, 3, 4, 5]
	for i in ships:
		keepGoing = True
		while keepGoing:
			try:
				placeX = random.randint(0, (10-i))
				placeY = random.randint(0, (10-i))
				# 0 will be north-south, 1 will be east to west
				direction = random.randint(0, 1)
				# Check that the placement isn't occupied
				if direction == 0:
					for j in range(placeY, (placeY + i)):
						if retGrid[j][placeX] == '*':
							raise Exception('The ship was placed on another ship, trying again')
				else:
					for j in range(placeX, (placeX + i)):
						if retGrid[placeY][j] == '*':
							raise Exception('The ship was placed on another ship, trying again')
				# Change the characters in the grid if they weren't occupied
								# Check that the placement isn't occupied
				if direction == 0:
					for j in range(placeY, (placeY + i)):
						retGrid[j][placeX] = '*'
				else:
					for j in range(placeX, (placeX + i)):
						retGrid[placeY][j] = '*'
				keepGoing = False
			except:
				pass
	return(retGrid)
		
	"""
	for i in range(len(retGrid)):
		for j in range(len(retGrid[i])):
			print(retGrid[i][j], end = '')
		print()
	"""
			
"""
gridList = [
	'    A   B   C   D   E   F   G   H   I   J',
	'  -----------------------------------------',
	' 1|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 2|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 3|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 4|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 5|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 6|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 7|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 8|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	' 9|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------',
	'10|   |   |   |   |   |   |   |   |   |   |',
	'  -----------------------------------------']
"""
print('This is a single player battleship game')
computerShips = placeShips()
printList(computerShips)
playerGrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
