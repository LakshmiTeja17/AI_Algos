#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from minmax import *
from gen import *
from alphabeta import *
from gui import *
import math
import time
import sys

def playGame():
	state = initState()
	scr, turtle = showGUI(state)
	print( "Press 1 for minimax, 2 for alpha beta pruning")
	algo = int(input())
	combo = []
	totalTime = 0
	totalNodes = [0]
	sizeofNode = sys.getsizeof(state)

	startTime = time.process_time() 
	
	while(True):
		#print( "State in driver is ")
		
		if( algo == 1):
			choice = minMax( state, totalNodes)
		else:
			choice = alphaBeta( state, totalNodes)
		if( choice == -1):
			print("Match drawn!!")
			break

		state = nextState(state, 'M', choice)
		scr, turtle = updateGUI( state['pos'][choice] - 1, choice, 'G', scr, turtle)
		for i in range(4):
			print(state['config'][i])
		print()
		
		combo = []
		if( isTerminal( state, combo) == 'G'):
			print( "Sorry!! You have lost!!")
			break

		
		print( "Choose your column (0-indexed). Choose 4 to exit")
		choice = int(input())
		if( choice == 4):
			break

		
		state = nextState( state, 'H', choice)
		scr, turtle = updateGUI( state['pos'][choice] - 1, choice, 'B', scr, turtle)
		
		

		for i in range(4):
			print( state['config'][i])
		print()
		
		combo = []
		if( isTerminal( state, combo) == 'B'):
			print( "Congrats!! You have won!!")
			break

		
	showWin( scr, turtle, combo)
	totalTime = time.process_time() - startTime
	print("Total time taken in seconds ", totalTime)
	print("Total nodes generated ", totalNodes[0])
	print("Size of node in bytes ", sizeofNode)
	print("Nodes generated per micro-second ", totalNodes[0]/(totalTime * 1000000))

	print()
	print("Press 'e' to exit or 'r' to play a new game")

	a = input()
	if( a == 'r'):
		playGame()
		


playGame()

		
	
