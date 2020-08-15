from DirtGenerator import dirtGenerator
from dfs import *
from bfs import *

#initState = dirtGenerator(10)
initState = ([[0 for i in range(10)] for j in range(10)], [0,0])
initState[1][1] = 1
initState[1][0] = 1
initState[0][1][3] =1 
for i in range(10):
	print (initState[0][i])

print("position is " + str( initState[1][0]) + ',' + str(initState[1][1]))
		
path = []
bfs( initState, path)
print(path) 



