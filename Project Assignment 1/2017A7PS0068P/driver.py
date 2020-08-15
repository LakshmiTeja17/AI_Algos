from DirtGenerator import *
from dfs import *
from bfs import *
from gui import *
import time
from turtle import *

print( "Input the percentage of dirt:")
import copy

percentage = int(input())
print( "Input the length of the room:")	
size = int(input())

initState = dirtGenerator(percentage,size)
initState1 = copy.deepcopy(initState)

from bfs import *
from dfs import *
from DirtGenerator import*

path1=[]
path2=[]


print("Enter your option")
# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

option = int( input())


if(option == 1):
	showGrid(size, initState1)
	exitonclick()

	
	

elif( option == 2):
	
	numNodes= [0]

	print( "Room is:")
	for i in range(size):
		print( initState[0][i])

	print("Position of vacuum cleaner is " + str( initState[1][0]) + ',' + str(initState[1][1]))	
	startTime = time.process_time()
	bfs( initState, path1, size, numNodes)
	totalTime = time.process_time() - startTime

	nodeSize = len(path1) + ( size*size ) + 2 
	totalCost = int((percentage * size * size)/100) + 2*len(path1) 

	print( "totalCost is " + str(totalCost))
	print( "Number of nodes created are " + str(numNodes))
	print( "Time taken " + str(totalTime))
	print("Node size is " + str(nodeSize))
	print( "Path is:")
	print(path1)
	
elif( option ==3):
	
	numNodes=[0]

	print( "Room is:")
	for i in range(size):
		print( initState[0][i])
	
	print("Position of vacuum cleaner is " + str( initState[1][0]) + ',' + str(initState[1][1]))		
	
	startTime = time.process_time()
	idfs( initState, path2, size, numNodes)
	totalTime = time.process_time() - startTime

	nodeSize = ( size*size ) + 2 
	totalCost = int((percentage * size * size)/100) + 2*len(path2) 

	print( "totalCost is " + str(totalCost))
	print( "Number of nodes created are " + str(numNodes))
	print( "Time taken " + str(totalTime))
	print("Node size is " + str(nodeSize))

	print( "Path is:")
	print(path2)

elif( option ==4):
	showGrid(size, initState)
	drawPath( initState1, path1, path2, size) 
	
