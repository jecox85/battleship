# James Cox
# 6-27-2020

"""
This is a single player version of the popular game called Battleship.
The ships will be randomly placed by the program, and the user will try to find them all.
There are 5 ships with lengths of 2, 3, 3, 4, and 5.
Misses will be marked with a 'O' and hits will be marked with an 'X'
"""

import random, sys
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

# This function returns a 10x10 grid of placed ships that will be used for the user to guess against
# The ships will be represented with a number representing their length for each point in the grid that they occupy
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
			# I used a try block because continues and breaks were only breaking out of the 1st loop and not the 2nd that I needed them to.
			# This way looks cleaner, and I can use the exceptions for logging later
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

# This function will take a an input string and make sure that it is a valid guess for the board
# ie. A1, B5, J10 etc
# This funcion will also print error messages to the console for the user.
# The function returns true if the input is valid and false otherwise
def validateGuess(inputString):
	returnBool = True
	# If the inputString isn't the right length set returnBool to False
	if len(inputString) != 2 and len(inputString) != 3: 						
		print('That is not a valid guess')
		returnBool = False
	# This checks that the first letter is between A and J inclusive
	elif ord(inputString[0].upper()) < 65 or ord(inputString[0].upper()) > 74:
		print('The given letter is invalid, please enter using format: C2')
		returnBool = False
	# This checks that the second number is between 1 and 9 inclusive
	elif ord(inputString[1]) < 49 or ord(inputString[1]) > 57:
		print('The given number is invalid, please enter using format: C2')
		returnBool = False
	# This checks that the third number is a 0 if the guess has a length of 3
	elif len(inputString) == 3 and ord(inputString[2]) != 48:
		print('The given number is invalid, please enter using format: C2')
		returnBool = False
	return returnBool
#end validateGuess

# Setup and user information for the game
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
print('Welcome to the game.')
print('This is a single player battleship game.')
print('The computer will place 5 ships on a 10x10 grid and it\'s your job to find them.')
print('The ships have lengths of 2, 3, 3, 4, and 5.')
keepGoing = True
# numOfHits will be used to check if we've found all of the ship locations.
numOfHits = 0
# totalGuesses will be used to let the user know how well they did at the end of the game.
totalGuesses = 0
# This is the main loop of the program
while keepGoing:
	print('Here is your board:')
	# printList(computerShips) #Uncomment this for easy testing
	printList(playerGrid)
	invalidInput = False
	guess = ''
	while not invalidInput:
		print('Please enter a guess, i.e. B2, or enter Q to quit.')
		guess = input()
		if len(guess) > 0 and guess[0].lower() == 'q':	# Allows the user to quit the game early
			print('Thanks for playing.')
			sys.exit()
		# Use function to validate user input
		invalidInput = validateGuess(guess)
	# ord('A') = 65, this will change that to 0 for use as the first index
	guessA = ord(guess[0].upper()) - 65
	# We've already validated that guess[1:] will be a number in validateGuess, this will subtract one to give us the proper index for the list
	guessB = int(guess[1:]) - 1	
	# If something is written in playerGrid, we've already guessed that spot
	if playerGrid[guessA][guessB] != ' ':
		print('You have already guessed that.')
	# if there isn't a space in computerships, that means a ship is in that location
	elif computerShips[guessA][guessB] != ' ':
		print('Hit')
		playerGrid[guessA][guessB] = 'X'
		numOfHits += 1
		totalGuesses += 1
	else:
		print('Miss')
		playerGrid[guessA][guessB] = 'O'
		totalGuesses += 1
	# The total number of ship locations is 17, this ends the game if we've found them all
	if numOfHits == 17:
		keepGoing = False
		printList(playerGrid)
		print('Congratulations, you have destroyed all of the ships.')
		print('You had a total of ' + str(totalGuesses) + ' guesses.')
		print('Thanks for playing.')