#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from copy import deepcopy

def initState():
	grid = []
	for i in range(4):
		row = []
		for j in range(4):
			row.append('0')
		grid.append(row)
	state = { 'config': grid, 'pos': [0,0,0,0]}
	return state

def nextState( state, player, column):
	if( state == None):
		return None
	if( state['pos'][column] == 4):
		return None
	next = deepcopy(state)
	color = 'B'
	if(player == 'M'):
		color = 'G'
	 
	next['config'][next['pos'][column]][column] = color
	next['pos'][column] += 1
	return next

def isTerminal( state, combo):
	if( state == None):
		return None

	#Check for rows
	for i in range(4):
		start = state['config'][i][0]
		end = state['config'][i][3]
		if( state['config'][i][1] == start and state['config'][i][2] == start ):
			if( start != '0'):
				combo.append([i,0])
				combo.append([i,1])
				combo.append([i,2])
				return start

		if( state['config'][i][1] == end and state['config'][i][2] == end):
			if( end!= '0'):
				combo.append([i,1])
				combo.append([i,2])
				combo.append([i,0])
				return end

		
	#Check for columns
	for i in range(4):
		row = state['pos'][i]
		if( row < 3):
			continue

		start = state['config'][row-1][i]
		if( state['config'][row-2][i] == start and state['config'][row-3][i] == start):
			combo.append([row-3,i])
			combo.append([row-2,i])
			combo.append([row-1,i]) 
			return start

	#Check for diagonals
	for i in range(2):
		for j in range(4):
			start = state['config'][i][j]
			if(j>1):
				if( state['config'][i+1][j-1] == start and state['config'][i+2][j-2] == start):
					if( start != '0'):
						combo.append( [i,j])
						combo.append( [i+1,j-1])
						combo.append( [i+2,j-2])						
						return start
			else:
				if( state['config'][i+1][j+1] == start and state['config'][i+2][j+2] == start):
					if( start != '0'):
						combo.append( [i,j])
						combo.append( [i+1,j+1])
						combo.append( [i+2,j+2])
						return start
	
	#Check if completely filled
	flag = 0
	for i in range(4):
		for j in range(4):
			if( state['config'][i][j] == '0'):
				flag =1
				break

	if (flag == 1):
		return 0

	else:
		return 'N'		


		  	
			

	


	
		
		
			
