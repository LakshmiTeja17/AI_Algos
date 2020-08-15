#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from gui import *
import time

def backtrack( domain_list, var_list, const_graph, choice, option, numNodes, recDepth, tdraw, screen):
	if( len(var_list) == len(domain_list) ):
		if( option == 'n'):
			print("The maximum growth of explicit stack is (R3): ", recDepth)
		return var_list
	
	numNodes[0]+=1
	
	if( numNodes[0]%100 == 0):
		print("The partial assignment at", numNodes[0], "number of nodes created is: ")
		for i in var_list:
			print( "N" + str(i+1) + " =", var_list[i])
		print()
		showAssignment( screen, tdraw, var_list, numNodes, choice, option) 
		time.sleep(1)

	num = selectVariable(domain_list, var_list, const_graph, choice)
	#print("Selected variable is", num)
	#ValueOrdering( domain_list, var_list, num)
		
	if( len(domain_list[num]) == 0):
		return False

	for value in domain_list[num]:
		if( isConsistent( value, num, var_list, const_graph) ):
			var_list[num] = value
			#print("Assigned value is:", value)
			result = backtrack( domain_list, var_list, const_graph, choice, option, numNodes, recDepth+1, tdraw, screen)
			if( result != False):
				return result

			del var_list[num]
			
	#print("??")
	return False

def selectVariable(domain_list, var_list, const_graph, choice):
	if( choice == 1):
		minimum = 1000000000
		num = 0
		for i in range(len(domain_list)):
			if i not in var_list:
				if( len(domain_list[i]) < minimum):
					minimum = len(domain_list[i])
					num = i	
		return num

	if( choice == 2):
		maximum = 0
		num = 0
		for i in range(len(const_graph)):
			if i not in var_list:
				if( len(const_graph[i]) > maximum):
					maximum = len(const_graph[i])
					num = i	
		return num 

	if(choice == 3):
		return len(var_list)	

def isConsistent( value, num, var_list, const_graph):
	consistent = True
	for i in const_graph[num]:
		if i in var_list:
			if( value == var_list[i]):
				consistent = False
				break

	return consistent 
