# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

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

path= []

while(True):
	print("Enter your option")



	option = int( input())


	if(option == 1):
		scr, t = showGrid(size, initState1)
		

			
			
	elif( option == 2):
		numNodes= [0]
	
		startTime = time.process_time()
		bfs( initState, path, size, numNodes)
		totalTime = time.process_time() - startTime
		nodeSize = len(path) + ( size*size ) + 2 
		totalCost = (percentage * size * size)/100 + 2*len(path) 
		
		print( "Path is:")
		print(path)
		
	elif( option ==3):
			
		numNodes=[0]
		startTime = time.process_time()
		idfs( initState, path, size, numNodes)
		totalTime = time.process_time() - startTime
		nodeSize = ( size*size ) + 2 
		totalCost = (percentage * size * size)/100 + 2*len(path) 
		print( "Path is:")
		print(path)

	elif( option ==4):
		scr, t= showGrid(size, initState)
		drawPath( scr, t, initState1, path, size) 

