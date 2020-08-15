# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

def goalTest( state, size):
	flag1 = True
	for i in range(size):
		for j in range(size):
			if( state[0][i][j] == 1):
				flag1 = False
	
	flag2 = False
	goalPos = [[0,0], [0,size-1], [size-1,0], [size-1,size-1]]
	for pos in goalPos:
		if( pos == state[1]): 
			flag2 = True

	if( flag1 == True and flag2 == True):
		return True
	else:
		return False


def nextState( state, action):
	if( action == 'MR'):
		state[1][1] += 1
						
	elif( action == 'ML'):
		state[1][1] -= 1
				
	elif( action == 'MU'):
		state[1][0] -= 1
				
	elif( action == 'MD'):
		state[1][0] += 1
					
	elif( action == 'S'):
		state[0][state[1][0]][state[1][1]] = 0

	return state
	
	
		
