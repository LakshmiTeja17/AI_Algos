#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from gen import *
from dfs_bt import *
from ac3 import *
import time
import sys
from copy import deepcopy
import turtle

def solveCSP( var_list, domain_list, const_graph, option, choice, tdraw, screen, results):
	startTime = time.process_time() 
	if(option == 'y'):
		if(AC3( domain_list, const_graph) == False):
			print("Sorry! No consistent solution exists.")
			return None
			for i in range(num_var):
				print("Domain lists are", domain_list[i])

	
	numNodes = [0]
	recDepth = 0

	result = backtrack( domain_list, var_list, const_graph, choice, option, numNodes, recDepth, tdraw, screen)
	totalTime = time.process_time() - startTime

	if( result != False):
		print( "Results:")
		for i in range(len(var_list)):
			print( "N" + str(i+1) + " =", var_list[i])
	
	else:
		print("Sorry! No consistent solution exists.")

	print()

	if(option == 'n'):
		if( choice!= 3):
			print("Number of nodes used with the hueristic(R5): ", numNodes[0])
			results[4] = numNodes[0]
		else:
			print("Number of nodes used (R1): ", numNodes[0])
			results[0] = numNodes[0]
			print("Memory used by each node in bytes (R2): ", sys.getsizeof(var_list) )
			results[1] = sys.getsizeof(var_list)
			#print("Maximum growth of implicit stack (R3): ", recDepth)
			print("Time taken in seconds (R4): ", totalTime)
			results[3] = totalTime
		return numNodes[0]

	if(option == 'y'):
		print("Number of nodes used (R6): ", numNodes[0])
		results[5] = numNodes[0]
		print("Time taken in seconds (R8): ", totalTime)
		results[7] = totalTime
		return numNodes[0]


tdraw = turtle.Turtle()
screen = turtle.Screen()
results= []
for i in range(8):
	results.append(-1)

option= input("The CSP is loaded with default values. Want to give custom input? Press y for yes or n for no: ")
if(option == 'n'): 
	num_var = 20
	var_list, domain_list, const_graph = init(num_var)
	loadDefaultDomains(domain_list)
	loadDefaultConstraintGraph( const_graph)

if(option == 'y'):
	num_var = int(input("Enter the number of variables in the CSP: "))
	var_list, domain_list, const_graph = init(num_var)
	loadDomains( domain_list)	
	loadConstraintGraph( const_graph) 

option = input( "Use AC3 as a pre-processing step? Press y for yes or n for no: ")
print()
choice = int(input( "Choose the heuristic to use. Press 1 for MRV or 2 for Degree hueristic or 3 for default ordering: "))
var_list1 = deepcopy(var_list)
var_list2 = deepcopy(var_list)
domain_list1 = deepcopy( domain_list)
domain_list2 = deepcopy( domain_list)

if( choice != 3):
	numNodes1 = solveCSP( var_list1, domain_list1, const_graph, 'n', 3, tdraw, screen, results)
numNodes2 = solveCSP( var_list, domain_list, const_graph, 'n', choice, tdraw, screen, results)


if(option == 'y'):
	numNodes2 = solveCSP( var_list2, domain_list2, const_graph, 'y', 3, tdraw, screen, results) 
	print( "The saving due to constraint propogation is (R7): ", (numNodes1 - numNodes2)/ numNodes1)
	results[6] = (numNodes1 - numNodes2)/ numNodes1

showResults(tdraw, screen, results)
	

turtle.exitonclick()






