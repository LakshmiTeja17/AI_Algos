#NAME: J LAKSHI TEJA
#ID: 2017A7PS0068P

from GUI import *
from math import *
import turtle
from bayesian import *
from time import *
import sys

listed = []

def btnclick(x, y):
	x = floor(x)
	y = floor(y)
	ansx=0
	ansy=0

	if x < 80 and y <-70 and y> -80 and x > 20:
		#print("generate clicked")
		if( len(cond_list)>20 or len(query_list) >20):
			displayAnswer(t,"Error!! Can't select more than 20 variables")
			return

		if( len(query_list) == 0):
			displayAnswer(t,"Error!! Choose atleast 1 query variable")
			sleep(5)
			return
			
			 
		#print( query_list)
		#print( cond_list)
		for var in listed:
			markov_blanket = computeMarkovBlanket( network, var)
			print("Markov Blanket of variable", var, ": ", markov_blanket)

		print()
		
		expression1 = ( query_list, cond_list)
		expression2 = ( cond_list,{})	
		string = 'P('
		for var in query_list:
			if( query_list[var] == 1):
				string += var + ','
			else:
				string += '~'+ var + ','
		string = string[:-1]+  "|"
		for var in cond_list:
			if( cond_list[var] == 1):
				string += var + ','
			else:
				string += '~'+ var + ','
		string = string[:-1] +  ')'
		num1 = computeProbability( network, expression1)
		num2 = computeProbability( network, expression2)
		prob = num1/num2
		print( "Probability is ", '%.20f'%(num1/num2))
		displayAnswer(t,string + " = " + '%.20f'%prob)
		return

	j = ceil( (x-23)/25)
	if( j!= floor((x-7)/25)):
		return

	i = floor( (85- y)/10)
	if( i!= ceil((80 - y)/10)):
		return
	    
	if listed[i] in cond_list or listed[i] in query_list :
		displayAnswer(t, "Error! Variable " + listed[i] + " already chosen")
		return
	clicked(t,i+1,j+1,listed)
	if( j+1<=2):                    
		if( j+1 == 1):
			query_list[listed[i]] = 1
		else:
			query_list[listed[i]] = 0
	else:
		if( j+1 == 3):
			cond_list[listed[i]] = 1
		else:
			cond_list[listed[i]] = 0
	    
	
	return

f = open( sys.argv[1])
network = createBayesianNetwork(f)
parent_list, cpt_list = network
listed = list(parent_list.keys())
#print( listed)

query_list = { }
cond_list = { }

screen, t = initialize_board()
list_boxes(t,listed)

turtle.onscreenclick(btnclick, 1)
turtle.listen()
turtle.done()
