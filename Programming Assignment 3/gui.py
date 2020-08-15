#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

from turtle import *

def showGUI(state):
	size = 4
	scr = Screen()
	t = Turtle()

	setup(800,800)
	tracer(0)
	length = 600/size;
	
	up()
	setpos(0,0)

	for i in range(-1,size):
		for j in range(-1,size):
			up()
			setpos( ((size/2) - i -1 ) * length, ((size/2) - j-1 ) * length)
			down()
			dot( length/20 , "black")
			
	up()

	for i in range(size):
		for j in range(size):
			if( state['config'][i][j] == 'B'):
				color = "blue"
			elif(  state['config'][i][j] == 'G'):
				color = "green"
			else:
				color = "white"
			up()
			setpos( -((size/2) - j - (1/2)) * length, ((size/2) - i - (1/2)) * length)
			dot( length/2 , color)
			
	return (scr, t)
			

def updateGUI( row, column, color, screen, turtle):
	size = 4

	if( color == 'B'):
		color = "blue"

	if( color == 'G'):
		color = "green"

	length = 600/size;
	
	turtle.setpos( -((size/2) - column - (1/2)) * length, ((size/2) - row - (1/2)) * length)
	turtle.dot( length/2 , color)
	up()
	
	return (screen, turtle)

def showWin( screen, turtle, combo):
	size = 4
	length = 600/size
	for pos in combo:
		turtle.setpos( -((size/2) - pos[1] - (1/2)) * length, ((size/2) - pos[0] - (1/2)) * length)
		turtle.dot( length/4 , "red")
	

		
	


