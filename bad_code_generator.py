#Kind of useless, as the check_victory is only set for size of 3
BOARD_SIZE = 3

SWITCH_PLAYER = [1, 0]

NUM_WHITE_SPACE = 2

PADDING = " " * NUM_WHITE_SPACE

PLAYER_CHAR = ['X', 'O']

BOARD = [[None for y in xrange(BOARD_SIZE)] for x in xrange(BOARD_SIZE)]

#Returns True/False for whether or not it has been updated or not
def update_board(x, y, player):
	if BOARD[y][x] == None:
		BOARD[y][x] = PLAYER_CHAR[player]
		return True
	return False

#The x and y values are in fact inverted, I don't like it but that's easier
def print_board(padding):
	for y in xrange(BOARD_SIZE):
		curr_string = ""
		for x in xrange(BOARD_SIZE):
			if BOARD[y][x] != None:
				curr_string += BOARD[y][x]
			else:
				curr_string += str(x + y * BOARD_SIZE + 1)
			curr_string += "|"
		print padding + "print '" + curr_string[:-1] + "'"
		if y != BOARD_SIZE - 1:
			print padding + "print '" + "-" * (BOARD_SIZE * 2 - 1) + "'"

#Lots of Magic Numbers here - essentially just checking all possible victory conditions. I'll fix this later
def check_victory(padding, curr_player):
	victory_condition = False
	if BOARD[0][0] != None:
		victory_condition = victory_condition or (BOARD[0][0] == BOARD[1][0] and BOARD[0][0] == BOARD[2][0])
		victory_condition = victory_condition or (BOARD[0][0] == BOARD[1][1] and BOARD[0][0] == BOARD[2][2])
		victory_condition = victory_condition or (BOARD[0][0] == BOARD[0][1] and BOARD[0][0] == BOARD[0][2])
	if BOARD[1][1] != None:
		victory_condition = victory_condition or (BOARD[1][1] == BOARD[2][0] and BOARD[1][1] == BOARD[0][2])
		victory_condition = victory_condition or (BOARD[1][1] == BOARD[0][1] and BOARD[1][1] == BOARD[2][1])
		victory_condition = victory_condition or (BOARD[1][1] == BOARD[1][0] and BOARD[1][1] == BOARD[1][2])
	if BOARD[2][2] != None:
		victory_condition = victory_condition or (BOARD[2][2] == BOARD[2][0] and BOARD[2][2] == BOARD[2][1])
		victory_condition = victory_condition or (BOARD[2][2] == BOARD[1][2] and BOARD[2][2] == BOARD[0][2])
	if victory_condition:
		print padding + "print '%s won!'" % (PLAYER_CHAR[curr_player])
		print padding + "return"
		return True
	return False

#TODO: Handle bad input (non integer)
def get_move(padding):
	print padding + "while move < 1 or move > 9 or BOARD[(move - 1) % 3][(move - 1) / 3] != None:"
	print padding + PADDING + "move = int(raw_input('Please enter a number 1-9 that has not been used '))"

def end_game(padding):
	print padding + "print 'Tie game!'"
	return

#Given a current board, acts out one move (poorly, may I add)
def generate_bad_tic_tac_toe(curr_depth = 1, curr_player = 0):
	padding = PADDING * curr_depth
	print_board(padding)
	victory = check_victory(padding, SWITCH_PLAYER[curr_player])
	if curr_depth == 10 or victory:
		if not victory:
			end_game(padding)
		return
	get_move(padding)
	for i in xrange(1, 10):
		pos = i - 1
		x = pos % BOARD_SIZE 
		y = pos / BOARD_SIZE
		if update_board(x, y, curr_player):
			print padding + "if move == %d:" % (i)
			generate_bad_tic_tac_toe(curr_depth + 1, SWITCH_PLAYER[curr_player])
			#Resets the board
			BOARD[y][x] = None

def make_bad_code():
	print "def play_tic_tac_toe():"
	print PADDING + "move = -1"
	generate_bad_tic_tac_toe()
	print "if __name__ == '__main__':"
	print PADDING + "play_tic_tac_toe()"

if __name__ == "__main__":
	make_bad_code()