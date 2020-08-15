#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

import turtle

def showAssignment( screen, tdraw, var_list, numNodes, choice, option):
	screen.clearscreen()
	
	string = "Heuristic: "
	if(choice == 1):
		string += "MRV\n"
	if(choice == 2):
		 string += "Degree\n"
	if(choice == 3):
		 string += "Default Ordering\n"

	if(option == 'y'):
		string+= "Using AC-3\n\n"
	if(option == 'n'):
		string+= "Not Using AC-3\n\n"
	
	
	string += "The partial assignment at " + str(numNodes[0]) + " number of nodes created is:\n"
	
	for i in var_list:
		string+=  ("N" + str(i+1) + " = " + str(var_list[i]) + "\n")

	tdraw.write(string, font=("Arial", 10, "normal"), align = "center" )

def showResults(tdraw, screen, results):
	screen.clearscreen()
	string = "RESULTS:\n"
	for i in range(8):
		string+= "R" + str(i+1) + ": " + str(results[i]) + "\n"

	tdraw.write(string, font=("Arial", 10, "normal"), align = "center" )
	

