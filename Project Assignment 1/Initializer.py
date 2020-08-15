import random

def dirtGenerator(p):
	count=0
	room = [[0 for i in range(10)] for j in range(10)] 
	while(count<20):
		temp1 = random.randint(0,9)
		temp2 = random.randint(0,9)
		if( room[temp1][temp2] != 1):
			room[temp1][temp2] = 1
			count = count+1
	
	position = [random.randint(0,9), random.randint(0,9)]
	initialState = (room, position)
	return initialState	
	#print(count)

#def createRootNode( initialState):
	

dirtGenerator(20)
		  	


		
	
