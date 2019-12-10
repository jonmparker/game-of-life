import random
from colorama import init
from colorama import Fore, Style

''' 
This program is based on the exercise on robertheaton.com titled Project 2: Game of Life
A board is create with randomized live cells. The board then changes state based on the 
state of its neighbors using the following rules:
	1) Any live cell with 0 or 1 neighbors becomes dead, because of underpopulation
	2) Any live cell with 2 or 3 neighbors stays alive, because its neighborhood is just right
	3) Any live cell with more than 3 live neighbors dies because of overpopulation
	4) Any dead cell with exactly 3 live neighbors becomes alive through reproduction
'''


# Construct a board with all cells initalized to 0, the dead state
# Parameters:
#	width: desired cell width of the board
#	height: desired cell height of the board
# Returns:
#	A board of dimensions width x height with all cells set to the dead state
def dead_state(width, height):
	board = [[0 for x in range(height)] for y in range(width)]

	return board


# Construct a board with all cells randomly initialized to either 1, the live state, or 0, the dead state
# Parameters:
#	width: desired cell width of the board
#	height: desired cell height of the board
# Returns:
#	A board of dimensions width x height with all cells randomly set to either the live state or the dead state
def random_state(width, height):
	board = dead_state(width, height)

	for i in range(width):
		for j in range(height):
			value = round(random.random())
			board[i][j] = value

	return board


# Print the board to the terminal with the live cells being represented as green dollar signs ($)
# Parameters:
#	board: a game board instance
# Returns:
#	Nothing
def render(board):
	init(autoreset=True)
	width = len(board)
	height = len(board[0])
	border_wid = width + 2
	temp = 0

	print(' ', end=' ')
	#print top border
	for x in range (border_wid):
		print(f'{Fore.YELLOW}~ ', end='')
	print('')
	for y in range(height):
		#print side border
		print(f'{Fore.BLUE}| ', end='')
		print(' ', end=' ')
		for x in range(width):
			temp = board[x][y]
			if(temp == 1):
				#transform live cells into green $
				print(f'{Fore.GREEN}$', end=' ')
			else:
				print(' ', end=' ')
		#print side border
		print(f'{Fore.BLUE} | ')
	print(' ', end=' ')
	for x in range (border_wid):
		print(f'{Fore.YELLOW}~ ', end='')
	print('')


# Determine the next state of a specific cell by checking its neighbor cells
# Parameters:
#	board: the current state of the game board
#	x: the width coordinate of the cell to be transformed
#	y: the length coordinate of the cell to be transformed
# Returns:
#	The new state of the cell being either a 1 for alive or a 0 for dead
def transform_cell(board, x, y):
	width = len(board)
	height = len(board[0])
	# the neighboring cells
	neighbor_tups = [(x, y)]
	neighbor_count = 0

	for i in range(x-1, x+2):
		# check to make sure the cell is on the board
		if i >=0 and i < width:
			for j in range(y-1, y+2):
				# check to make sure the cell is on the board
				if j >= 0 and j < height:
					# check to make sure we haven't counted this cell yet
					if not (i, j) in neighbor_tups:
						neighbor_tups.append(tuple((i, j)))

	for (x1, y1) in neighbor_tups:
		#make sure we don't count the current cell as a neighbor cell
		if(x1 != x and y1 != y):
			if board[x1][y1] == 1:
				neighbor_count += 1

	if board[x][y] == 1:
		if neighbor_count <=1 or neighbor_count > 3:
			return 0
		else:
			return 1
	else:
		if neighbor_count == 3:
			return 1
		else:
			return 0




# Determines the next state the board will take
# Parameters:
#	board: the current state of the game board
# Returns:
#	A board that has been transformed to the next state
def next_board_state(board):
	width = len(board)
	height = len(board[0])
	new_state = dead_state(width, height)

	for x in range(width):
		for y in range(height):
			new_state[x][y] = transform_cell(board, x, y)

	return new_state

# Run the program forever, must be terminated to stop
def run_forever(start):
	board = start
	render(board)

	while True:
		board = next_board_state(board)
		render(board)

if __name__ == "__main__":
	start = random_state(20, 50)
	run_forever(start)
