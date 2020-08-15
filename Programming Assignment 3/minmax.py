#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from gen import *

def minMax( state, totalNodes):
	maximum = -2
	col = -1
	for i in range(4):
		#print(state)
		next = nextState( state, 'M', i)
		totalNodes[0]+=1
		#print(next)
		if( next!= None) :
			
			for j in range(4):
				print(next['config'][j])
			value = minValue(next,0, totalNodes)

			if( value > maximum):
				maximum = value
				col = i

	return col

def maxValue( state, depth, totalNodes):
	if( isTerminal(state, []) == 'B'):
		#print(" maxValue terminal B")	
		return -1

	if( isTerminal(state, []) == 'G'):
		#print(" maxValue terminal G")
		return 1

	if( isTerminal(state, []) == 'N'):
		#print(" maxValue terminal N")
		return 0

	maximum = -2
	for i in range(4):
		next = nextState( state, 'M', i)
		totalNodes[0]+=1
		#if( next != None):
			#print( "State in maxValue is ")
			#for j in range(4):
				#print(next['config'][j])
		if( next!= None) :
			value = minValue(next, depth+1, totalNodes)
			#print( "utility of next in maxValue is ", value, depth)
			if( value > maximum):
				maximum = value
	
	return maximum

def minValue( state, depth, totalNodes):
	if( isTerminal(state, []) == 'B'):
		#print(" minValue terminal B")	
		return -1

	if( isTerminal(state, []) == 'G'):
		#print(" minValue terminal G")
		return 1

	if( isTerminal(state, []) == 'N'):
		#print(" minValue terminal N")
		return 0

	minimum = 2
	for i in range(4):
		next = nextState( state, 'H', i)
		totalNodes[0]+=1		
		#if( next != None):
			#print( "State in minValue is ")
			#for j in range(4):
			#	print(next['config'][j])
		if( next!= None) :
			value = maxValue(next, depth+1, totalNodes)
			#print( "utility of next in minValue is ", value, depth)
			if( value < minimum):
				minimum = value
	return minimum
			
		
 	 
