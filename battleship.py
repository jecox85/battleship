# James Cox
# 6-27-2020

"""
This is a single player battleship game.
The ships will be randomly placed, and the user will try to find them all.

create a function to randomly place the ships and return a grid to store
Create two lists, one for the ships, and one for the board.
create a function to print a pretty version of the board, O's for guesses and X's for hits
Implement gameplay
	keep a total of hits and add 1 to each hit.  end game when the total ='s the total available hits

"""

import random, sys, re
# This function will take an input of a 10 x 10 list and print a board to the console.
def printList(inputList):
	print('    1   2   3   4   5   6   7   8   9   10')
	print('  -----------------------------------------')
	for i in range(10):
		print(' ' + chr(i + 65) + '| ', end = '')
		for j in range(10):
			print(inputList[i][j], end = '')
			print(' | ', end = '')
		print()
		print('  -----------------------------------------')
	
		
# end printList	

# This function returns a grid of the placed ships
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
		while True:
			try:
				placeX = random.randint(0, (10-i))
				placeY = random.randint(0, (10-i))
				# 0 will be north-south, 1 will be east to west
				direction = random.randint(0, 1)
				# Check that the placement isn't occupied, raise an exception to try again if they are.
				if direction == 0:
					for j in range(placeY, (placeY + i)):
						if retGrid[j][placeX] == '*':
							raise Exception('The ship was placed on another ship, trying again')
				else:
					for j in range(placeX, (placeX + i)):
						if retGrid[placeY][j] == '*':
							raise Exception('The ship was placed on another ship, trying again')
				# Change the characters in the grid if they weren't occupied
				if direction == 0:
					for j in range(placeY, (placeY + i)):
						retGrid[j][placeX] = '*'
				else:
					for j in range(placeX, (placeX + i)):
						retGrid[placeY][j] = '*'
				break
			except:
				pass
	return(retGrid)
# end placeShips	
# This function will take a an input string and make sure that it is a valid guess for the board
# ie. A1, B5, J10 etc
# This funcion will also print error message to the console for the user.
# The function returns true if the input is valid and false otherwise
def validateGuess(inputString):
	returnBool = True
	if len(inputString) != 2 and len(inputString) != 3: 						# If the inputString isn't the right length
		print('That is not a valid guess')
		returnBool = False
	elif ord(inputString[0].upper()) < 65 or ord(inputString[0].upper()) > 74: 	# This checks that the first letter is between A and J inclusive
		print('The given letter is invalid, please enter using format: C2')
		returnBool = False
	elif ord(inputString[1]) < 49 or ord(inputString[1]) > 57:					# This checks that the second number is between 1 and 9 inclusive
		print('The given number is invalid, please enter using format: C2')
		returnBool = False
	elif len(inputString) == 3 and ord(inputString[2]) != 48:					# This checks that the third number is a 0 if the guess has a length of 3
		print('The given number is invalid, please enter using format: C2')
		returnBool = False
	return returnBool

# Setup
random.seed()
computerShips = placeShips()
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
print('This is a single player battleship game')
print('The computer will place 5 ships on a 10x10 grid and it\'s your job to find them.')

keepGoing = True
numOfHits = 0
totalGuesses = 0
while keepGoing:
	print('Here is your board, please make a guess.  Example: B2')
	printList(playerGrid)
	invalidInput = False
	guess = ''
	while not invalidInput:
		print('Please enter a guess.')
		guess = input()
		invalidInput = validateGuess(guess)			# Use function to validate user input
	guessX = ord(guess[0].upper()) - 65				# Added an extra variable to make it more readable
	guessY = int(guess[1:]) - 1						# Added an extra variable to make it more readable
	if playerGrid[guessX][guessY] != ' ':
		print('You have already guessed that')
	elif computerShips[guessX][guessY] == '*':
		print('Hit')
		playerGrid[guessX][guessY] = 'X'
		numOfHits += 1
		totalGuesses += 1
	else:
		print('Miss')
		playerGrid[guessX][guessY] = 'O'
		totalGuesses += 1
	if numOfHits == 17:
		keepGoing = False
		printList(playerGrid)
		print('Congratulations, you have sunk all of the ships')
		print('You had a total of ' + str(totalGuesses) + ' guesses')