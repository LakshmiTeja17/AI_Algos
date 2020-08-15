# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

import random

def dirtGenerator(p, size):
	count=0
	room = [[0 for i in range(size)] for j in range(size)] 
	while(count< (p*size*size)/100):
		temp1 = random.randint(0,size-1)
		temp2 = random.randint(0,size-1)
		if( room[temp1][temp2] != 1):
			room[temp1][temp2] = 1
			count = count+1
	
	position = [random.randint(0,size-1), random.randint(0,size-1)]
	initialState = (room, position)
	return initialState	
	#print(count)

#def createRootNode( initialState):
	


		  	


		
	
