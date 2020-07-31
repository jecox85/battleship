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
placeShips()