# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

import queue
from gen import *
import copy

def bfs( initState, path, size, numNodes):
	
	frontier= queue.Queue()
	

	if( initState[0][ initState[1][0] ][initState[1][1]] == 1): 
		initState[0][ initState[1][0] ][initState[1][1]] = 0	
	
	if(goalTest(initState,size) == True):
		return 1

	explored = { tuple(path)}
	frontier.put( (initState, []))
	numNodes[0]+= 1
	
	try:
		
		while(True):
			
			node = frontier.get()
			state = node[0]
			nextStates = []
			nextPaths = []
			nextNodes = []
			
			if( state[1][1] != size-1):
				nextStates.append(copy.deepcopy(node[0]))
				nextPaths.append(copy.deepcopy(node[1]))
				nextState( nextStates[-1], 'MR')
				nextPaths[-1].append('MR')
			
			if( state[1][1]!= 0):
				nextStates.append(copy.deepcopy(node[0]))
				nextPaths.append(copy.deepcopy(node[1]))
				nextState( nextStates[-1], 'ML')
				nextPaths[-1].append('ML')

			if( state[1][0]!= 0):
				nextStates.append(copy.deepcopy(node[0]))
				nextPaths.append(copy.deepcopy(node[1]))			
				nextState( nextStates[-1], 'MU')
				nextPaths[-1].append('MU')

			if( state[1][0]!= size-1):
				nextStates.append(copy.deepcopy(node[0]))
				nextPaths.append(copy.deepcopy(node[1]))
				nextState( nextStates[-1], 'MD')
				nextPaths[-1].append('MD')
			
			for i in range(len(nextStates)):	
				if( nextStates[i][0][ nextStates[i][1][0] ][nextStates[i][1][1]] == 1): 
					nextStates[i][0][ nextStates[i][1][0] ][nextStates[i][1][1]] = 0
			
				if tuple(nextPaths[i]) not in explored:
				
					if( goalTest(nextStates[i], size) == True):
						for dir in nextPaths[i]:
							path.append(dir)
						return 1

					else:
						#print(nextPaths[i])
						#print( str(nextStates[i][1][0]) + ',' + str(nextStates[i][1][1]))
						explored.add( tuple(nextPaths[i]))
						frontier.put( (nextStates[i], nextPaths[i]))
						numNodes[0]+= 1
					
		
						
	except MemoryError:
		print(" Memory out of bounds!!")
		return -1		

