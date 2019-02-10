import random

def printBoard(board):
	# Prints the current status of the board on to the screen
	print('\n'*3)
	print(" "*35+"|     |     ")
	print(" "*32+board[1]+"  |  "+board[2]+"  |  "+board[3]+"     ")
	print(" "*31+"____|_____|_____")
	print(" "*35+"|     |     ")
	print(" "*32+board[4]+"  |  "+board[5]+"  |  "+board[6]+"     ")
	print(" "*31+"____|_____|_____")
	print(" "*35+"|     |     ")
	print(" "*32+board[7]+"  |  "+board[8]+"  |  "+board[9]+"     ")
	print(" "*31+"    |     |     ")	

def clearBoard(board):
	# Clears the board
	board = [" "]*10


def PlayAgain():
	# Gives player choice to play again.
	print('\n'*2)
	cont = input("  Want to play again?(Y/N)")
	while(cont != 'Y' and cont != 'N'):
		cont = input("  Invalid input. Enter Y if you want to play again N if you don't. ")
	if(cont == 'Y'):
		return True
	return False


def XO():
	# Gives player choice to play as X or O and assigns other to computer
	choice = input("  Want to play as X or O? ")
	while(choice != 'X' and choice != 'O'):
		choice = input("  Invalid input. Pick X or O.")
	if(choice == 'X'):
		return ['X', 'O']

	return ['O', 'X']


def FirstPlay():
	# Randomly chooses whther player or computer goes first
	x = random.randint(1,2)
	if(x == 1):
		return 'player'
	return 'computer'


def CheckWin(board, choice):
	# Checks whether either the computer or player has won.
	return ((board[1] == choice and board[2] == choice and board[3] == choice) or
		   (board[4] == choice and board[5] == choice and board[6] == choice) or
		   (board[7] == choice and board[8] == choice and board[9] == choice) or
		   (board[1] == choice and board[4] == choice and board[7] == choice) or
		   (board[2] == choice and board[5] == choice and board[8] == choice) or
		   (board[3] == choice and board[6] == choice and board[9] == choice) or
		   (board[1] == choice and board[5] == choice and board[9] == choice) or
		   (board[3] == choice and board[5] == choice and board[7] == choice)) 


def CompMove(board, cchoice, pchoice):
	# The computer moves based on the following criteria in order
	# 1. Checks if it can win in the next turn and does that move
	# 2.  If not then Checks whether the player can win in the next turn and blocks them
	# 3. Else it checks available corners and randomly occupies one of them
	# 4. Else it checks whether the center is empty and occupies that.
	# 4. Else it checks for an available side and randomly occupies one.
	# 5. Else it return none.

	print("\n\n  Computer's Move")
	dup_list = board.copy() #Duplicate list of the board so that the computer can perform the available moves 
							# and check whether it or the player can win. 

	for i in range(1,10):
		if(dup_list[i] == " "):
			dup_list[i] = cchoice
			if(CheckWin(dup_list, cchoice)):
				return i
			else:
				dup_list[i] = " "

	for i in range(1, 10):
		if(dup_list[i] == " "):
			dup_list[i] = pchoice
			if(CheckWin(dup_list, pchoice)):
				return i
			else:
				dup_list[i] = " "

	corners = [1, 3, 7, 9]
	avail_corner = []
	for i in corners:
		if(board[i] == " "):
			avail_corner.append(i)
	if(avail_corner):
		return random.choice(avail_corner)

	if(board[5] == " "):
		return 5

	sides = [2, 4, 6, 8]
	avail_sides = []
	for i in sides:
		if(board[i] == " "):
			avail_sides.append(i)
	if(avail_sides):
		return random.choice(avail_sides)

	return None  


def PlayerMove(board, pchoice):
	# Function to allow the player to make a move

	print("\n \n")
	avail_moves = []
	for i in range(1,10):
		if(board[i] == " "):
			avail_moves.append(i)
	if(avail_moves):
		x = int(input("  Player's Turn. Input move: "))
		if(x in avail_moves):
			return x
		else:
			while(x not in avail_moves):
				x = int(input("  That is not a valid move. Enter again"))
		return x
	else:
		return None


print(" TIC TAC TOE".center(80))

while(True):
	board = [" "]*10 # Initialisesthe board. 
	print("\n"*3)
	pchoice, cchoice = XO()
	print("\n")
	print("  You are {}. Computer is {}.".format(pchoice, cchoice))
	play = FirstPlay()
	print("\n\n  {} goes first.".format(play.capitalize()))
	t = 0
	while(t<10):
		if(play == 'computer'):
			move = CompMove(board, cchoice, pchoice)
			if(move):
				board[move] = cchoice
				printBoard(board)
				if(CheckWin(board, cchoice)):
					print("\n \n  Computer Wins.")
					break
			else:
				print("\n\n  Match Tied.")
				t = 11
			play = 'player'
			t += 1
		else:
			move = PlayerMove(board, pchoice)
			if(move):
				board[move] = pchoice
				printBoard(board)
				if(CheckWin(board, pchoice)):
					print("\n \n  Player Wins.")
					break
			else:
				print("\n\n  Match Tied.")
				t = 11
				break
			play = 'computer'
			t += 1



	if(not (PlayAgain())):
		break
