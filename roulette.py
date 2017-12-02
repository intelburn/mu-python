import random
#use cryptographically strong random number generator for overkill
sec_random=random.SystemRandom()
#make the list of colors. This is to reduce the number of lines in the roulette_wheel function
def make_colors(color, num):
	#make a long string from the arguement in the quantity of the arguement
	colors=(color+",")*int(num)
	#trim off the trailing comma
	colors=colors[:-1]
	#seperate the long string into a list
	colors_list=colors.split(',')
	#return the list
	return colors_list
#Function for simulating the roulette wheel.
#The zeros arguement is an int and is used to determine whether or not the board is a single zero board or a double zero board
#The guess arguement is a string and is used to determine what to use as the win condition
#The bet arguement is the amount of the wager
#The bet will be returned either positive or negative depending on the result of the round
def roulette_wheel(zeros, guess, bet):
	#create empty board list
	board=[]
	#add the red to the board
	board.extend(make_colors('red', 18))
	#add the black to the board
	board.extend(make_colors('black', 18))
	#add the green to the board using the zeros arguement
	board.extend(make_colors('green', int(zeros)))
	#use the the system's hardware random number generator to pick a result
	result=sec_random.choice(board)
	#determine if the guess was correct
	if(guess.lower()==result):
		#return the winning
		return int(bet)
	else:
		#return the loss
		return int(bet)*-1
#loop of the number of zeros in the session
for zeros in [1, 2]:
	#loop for the rounds in the session
	for rounds in [5, 100, 1000]:
		#reset the winnings
		pot=0
		#loop for the guessing strategy
		for kind in ['red', 'black', 'rand']:
			#check for random round
			if kind=='rand':
				#loop for determining the results of all of the rounds
				for num in range(0, rounds):
					#play the game
					pot+=roulette_wheel(zeros, sec_random.choice(['red', 'black']), 100)
			#play a game with a static guess
			else:
				#loop for determining the results of all of the rounds
				for num in range(0, rounds):
					#play the game
					pot+=roulette_wheel(zeros, kind, 100)
			#print the results of the session
			print("After %d rounds using %d zeros using a %s choice and betting $100 each time the pot is at $%d." % (rounds, zeros, kind, pot))
