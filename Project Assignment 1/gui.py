# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

from turtle import *

def showGrid( size, initState):

	#scr = screen()
	scr=1
	t = Turtle()

	setup(650,650)
	speed(50)
	
	tracer(0)
	length = 600/size;
	
	up()
	
	setpos(0,0)
	for i in range(-1,size):
		for j in range(-1,size):
			
			#setheading(0)
			
			if(size%2==0):
				up()
				setpos( ((size/2) - i -1 ) * length, ((size/2) - j-1 ) * length)
				down()
				dot( length/20 , "black")
				'''for i in range(4):
					
					forward(length)
					right(90)'''
				
					
			else:
				up()
				setpos( (int(size/2) - i- (1/2))*length, (int(size/2) - j- (1/2))*length)
				down()
				dot( length/20 , "black")
				'''for i in range(4):
					forward(length)
					right(90)'''

	
	#cleaner = Turtle()
	up()
	#print( initState[1][0])
	#print(initState[1][1])
	
	for i in range(size):
		for j in range(size):
			if( initState[0][i][j] == 1):
				up()
				if(size%2==0):
					setpos( -((size/2) - j - (1/2)) * length, ((size/2) - i - (1/2)) * length)
					print(i, end = ' ')
					print(j)
					dot( length/2 , "blue")

				else:
					setpos( -(int(size/2) - j)*length, (int(size/2) - i)*length)
					dot( length/2 , "blue")

	tracer(1)	

	if(size%2==0):
		setpos( -((size/2) - initState[1][1] - (1/2)) * length, ((size/2) - initState[1][0] - (1/2)) * length)
		shape("square")
		shapesize( length/40, length/40)
	
	else:
		setpos( -(int(size/2) - initState[1][1])*length, (int(size/2) - initState[1][0])*length)
		shape("square")
		shapesize( length/40, length/40)

	for i in range(size):
		print( initState[0][i])

	print("position is " + str( initState[1][0]) + ',' + str(initState[1][1]))

	return (scr, t)




def drawPath(  scr, t, initState, path, size):

	length = 600/size;
	
	#t.shape("arrow")
	up()

	if(size%2==0):
		t.setpos( -((size/2) - initState[1][1] - (1/2)) * length, ((size/2) - initState[1][0] - (1/2)) * length)
		t.shape("arrow")
		t.shapesize( length/40, length/40)
	
	else:
		t.setpos( -(int(size/2) - initState[1][1])*length, (int(size/2) - initState[1][0])*length)
		t.shape("arrow")
		t.shapesize( length/40, length/40)	

	
	speed(1)
	t.pensize(5)
	t.pencolor("red")
	down()
	tracer(1)

	for action in path:
		t.setheading(0)
		if( action == 'MR'):
			t.forward(length)

		if( action == 'ML'):
			t.backward(length)

		if( action == 'MU'):
			t.left(90)
			t.forward(length)

		if( action == 'MD'):
			t.right(90)
			t.forward(length)

	exitonclick()
		
	
	



	
