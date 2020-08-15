#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from gen import *

def alphaBeta( state, totalNodes):
	value = -2
	col = -1
	alpha = -2
	beta = 2
	for i in range(4):
		next = nextState( state, 'M', i)
		totalNodes[0]+=1
		if( next!= None) :
			temp = minValue(next,alpha, beta,  0, totalNodes)
			if( value < temp):
				value = temp
				col = i
			if( value >= beta):
				return value
			if( alpha < value):
				alpha = value

	return col

def maxValue( state, alpha, beta, depth, totalNodes):
	if( isTerminal(state, []) == 'B'):
		#print(" minValue terminal B")	
		return -1

	if( isTerminal(state, []) == 'G'):
		#print(" minValue terminal G")
		return 1

	if( isTerminal(state, []) == 'N'):
		#print(" minValue terminal N")
		return 0

	value = -2
	for i in range(4):
		next = nextState( state, 'M', i)
		totalNodes[0]+=1	
		if( next!= None) :
			temp = minValue( next,alpha, beta,  depth+1, totalNodes)
			if( value < temp):
				value = temp
			if( value >= beta):
				return value
			if( alpha < value):
				alpha = value

	return value

def minValue( state, alpha, beta, depth, totalNodes):
	if( isTerminal(state, []) == 'B'):
		#print(" minValue terminal B")	
		return -1

	if( isTerminal(state, []) == 'G'):
		#print(" minValue terminal G")
		return 1

	if( isTerminal(state, []) == 'N'):
		#print(" minValue terminal N")
		return 0

	value = 2
	for i in range(4):
		next = nextState( state, 'H', i)
		totalNodes[0]+=1
		if( next!= None) :
			temp = maxValue(next,alpha, beta,  depth+1, totalNodes)
			if( value > temp):
				value = temp
			if( value <= alpha):
				return value
			if( beta > value):
				beta = value

	return value


	
