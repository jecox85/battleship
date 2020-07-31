# James Cox
# 7-13-2020

"""
This is a single player version of the popular game called Battleship.
The ships will be randomly placed by the program, and the user will try to find them all.
There are 5 ships with lengths of 2, 3, 3, 4, and 5.
Misses will be marked with a 'O' and hits will be marked with an 'X'

Battleship boards methods and variables will be stored in a separate class in the Battleship.py file
"""

import sys, logging
logging.basicConfig(filename='BattleshipLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
try:
	from Battleship import Battleship
	logging.debug('Loading modules.')
except:
	logging.critical('Missing required class file')
	sys.exit()

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
		logging.debug('User input was not the right length.')
	# This checks that the first letter is between A and J inclusive
	elif ord(inputString[0].upper()) < 65 or ord(inputString[0].upper()) > 74:
		print('The given letter is invalid, please enter using format: C2')
		returnBool = False
		logging.debug('User input had first character that wasn\'t between A and J')
	# This checks that the second number is between 1 and 9 inclusive
	elif ord(inputString[1]) < 49 or ord(inputString[1]) > 57:
		print('The given number is invalid, please enter using format: C2')
		returnBool = False
		logging.debug('User input had second character that wasn\'t between 1 and 9 inclusive.')
	# This checks that the third number is a 0 if the guess has a length of 3
	elif len(inputString) == 3 and ord(inputString[2]) != 48:
		print('The given number is invalid, please enter using format: C2')
		returnBool = False
		logging.debug('User input had third character that wasn\'t a 0')
	return returnBool
#end validateGuess
	
# Setup and user information for the game
print('Welcome!')
print('This is a single player battleship game.')
print('The computer will place 5 ships on a 10x10 grid and it\'s your job to find them.')
print('The ships have lengths of 2, 3, 3, 4, and 5.')
keepGoing = True
thisGame = Battleship()
# This is the main loop of the program
while keepGoing:
	print('Here is your board:')
	logging.debug('Computer\'s board:\n' + thisGame.computerBoard())
	print(thisGame.userBoard())
	invalidInput = False
	guess = ''
	while not invalidInput:
		print('Please enter a guess, i.e. B2, or enter Q to quit.')
		guess = input()
		if len(guess) == 1 and guess[0].lower() == 'q':	# Allows the user to quit the game early
			print('Thanks for playing.')
			logging.debug('User has exited the program')
			sys.exit()
		# Use function to validate user input
		invalidInput = validateGuess(guess)
	# ord('A') = 65, this will change that to 0 for use as the first index
	guessA = ord(guess[0].upper()) - 65
	# We've already validated that guess[1:] will be a number in validateGuess, this will subtract one to give us the proper index for the list
	guessB = int(guess[1:]) - 1	
	# If something is written in playerGrid, we've already guessed that spot
	if thisGame.playerGrid[guessA][guessB] != ' ':
		print('You have already guessed that.')
	# if there isn't a space in computerGrid, that means a ship is in that location
	elif thisGame.computerGrid[guessA][guessB] != ' ':
		print('Hit')
		thisGame.playerGrid[guessA][guessB] = 'X'
		thisGame.numOfHits += 1
		logging.debug('numOfHits increased by 1 and = ' + str(thisGame.numOfHits))
		thisGame.totalGuesses += 1
		logging.debug('totalGuesses increased by 1 and = ' + str(thisGame.totalGuesses))
	else:
		print('Miss')
		thisGame.playerGrid[guessA][guessB] = 'O'
		thisGame.totalGuesses += 1
		logging.debug('totalGuesses increased by 1 and = ' + str(thisGame.totalGuesses))
	# The total number of ship locations is 17, this ends the game if we've found them all
	if thisGame.numOfHits == 17:
		keepGoing = False
		print(thisGame.userBoard())
		print('Congratulations, you have destroyed all of the ships.')
		print('You had a total of ' + str(thisGame.totalGuesses) + ' guesses.')
		print('Thanks for playing.')