# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

from gen import *



def dfs( state, depth, limit, path, size, numNodes):

	flag=0

	#print(path)
	#print( str(state[1][0]) + ',' + str(state[1][1]))
	
	if(goalTest(state, size) == True):
		return 1
	else: 
		
		if(depth == limit):
			#print("limit reached")
			return -1 
	
		else:
			
			
			
			if( state[0][state[1][0]][state[1][1]] == 1):
				nextState( state, 'S')
				flag=1
			
			if( state[1][1] != size-1):
				path.append('MR')
				
				result = dfs( nextState( state, 'MR'), depth+1, limit,path,size, numNodes )
				numNodes[0]+=1
				if( result != -1):
					return 1
				
				nextState( state, 'ML')
				path.pop()
			if( state[1][1]!= 0):
				path.append('ML')
				
				result = dfs( nextState( state, 'ML'), depth+1, limit,path, size,numNodes )
				numNodes[0]+=1
				if( result != -1):
					return 1
				
				nextState( state, 'MR')
				path.pop()
			if( state[1][0]!= 0):
				path.append('MU')
				
				result = dfs( nextState( state, 'MU'), depth+1, limit,path, size, numNodes )
				numNodes[0]+=1
				if( result != -1):
					return 1
				
				nextState( state, 'MD')
				path.pop()
			if( state[1][0]!= size-1):
				path.append('MD')
				
				result = dfs( nextState( state, 'MD'), depth+1, limit,path, size, numNodes )
				numNodes[0]+=1
				if( result != -1):
					return 1
				
				nextState( state, 'MU')
				path.pop()

			if(flag==1):
				state[0][state[1][0]][state[1][1]] = 1
			
			#print("final " + str(state[0][1][2]))

	
	
	return -1

	
	


def idfs( state,path, size, numNodes):
	limit =0
	try:
		while(True):
			result = dfs( state, 0, limit, path, size, numNodes)
			if( result != -1):
				break
			#print( "dfs with limit " + str(limit) + " not possible")
			limit+=1
		
		return path


	except MemoryError:
		print(" Memory out of bounds!!")
		return -1

		
			
		  
	

			
		 
