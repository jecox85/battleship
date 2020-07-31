# James Cox
# 7-13-2020
import random

class Battleship():
	# This class contains the user boards and methods for a
	# single player battleship game against a computer.
	
	def __init__(self):
		random.seed()
		self.computerGrid = self._placeShips()
		self.playerGrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
				
		# numOfHits will be used to check if we've found all of the ship locations.
		self.numOfHits = 0
		# totalGuesses will be used to let the user know how well they did at the end of the game.
		self.totalGuesses = 0
	
	# This function returns a 10x10 grid of placed ships that will be used for the user to guess against
	# The ships will be represented with a number representing their length for each point in the grid that they occupy
	def _placeShips(self):
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
			while True:
				# I used a try block because continues and breaks were only breaking out of the 1st loop and not the 2nd that I needed them to.
				try:
					# 0 will be north-south, 1 will be east to west
					direction = random.randint(0, 1) 		
					if direction == 0:
						placeX = random.randint(0, 9)
						placeY = random.randint(0, (10-i))
					else:
						placeX = random.randint(0, (10-i))
						placeY = random.randint(0, 9)
					# Check that the placement isn't occupied, raise an exception to try again if they are.
					if direction == 0:
						for j in range(placeY, (placeY + i)):
							if retGrid[j][placeX] != ' ':
								raise Exception('The ship was placed on another ship, trying again')
					else:
						for j in range(placeX, (placeX + i)):
							if retGrid[placeY][j] != ' ':
								raise Exception('The ship was placed on another ship, trying again')
					# Change the characters in the grid if they weren't occupied
					if direction == 0:
						for j in range(placeY, (placeY + i)):
							retGrid[j][placeX] = str(i)
					else:
						for j in range(placeX, (placeX + i)):
							retGrid[placeY][j] = str(i)
					break
				except:
					pass
		return(retGrid)
	# end placeShips	
	
	# This function will take an input of a 10 x 10 list and return a game board within a string.
	def userBoard(self):
		board = ''
		board += '    1   2   3   4   5   6   7   8   9   10\n'
		board += '  -----------------------------------------\n'
		for i in range(10):
			board += ' ' + chr(i + 65) + '| '
			for j in range(10):
				board += self.playerGrid[i][j]
				board += ' | '
			board += '\n'
			board += '  -----------------------------------------\n'
		return board
	# end userBoard	
	
		# This function will take an input of a 10 x 10 list and return a game board within a string.
	def computerBoard(self):
		board = ''
		board += '    1   2   3   4   5   6   7   8   9   10\n'
		board += '  -----------------------------------------\n'
		for i in range(10):
			board += ' ' + chr(i + 65) + '| '
			for j in range(10):
				board += self.computerGrid[i][j]
				board += ' | '
			board += '\n'
			board += '  -----------------------------------------\n'
		return board
	# end computerBoard	
