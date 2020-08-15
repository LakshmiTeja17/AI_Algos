# ID: 2017A7PS0068P
# NAME: J LAKSHMI TEJA

from turtle import *

def showGrid( size, initState):
	setup(650,650)
	speed(1)
	
	tracer(0)
	length = 600/size;
	shape("arrow")
	shapesize( length, length)


	up()
	#tracer(1)
	goto(0,0)
	for i in range(size):
		for j in range(size):
			
			#setheading(0)
			
			if(size%2==0):
				up()
				goto( ((size/2) - i -1 ) * length, ((size/2) - j-1 ) * length)
				down()
				for i in range(4):
					
					forward(length)
					right(90)
			else:
				up()
				goto( (int(size/2) - i- (1/2))*length, (int(size/2) - j- (1/2))*length)
				down()
				for i in range(4):
					forward(length)
					right(90)

	
	#cleaner = Turtle()
	up()
	#print( initState[1][0])
	#print(initState[1][1])
	if(size%2==0):
		goto( ((size/2) - initState[1][0] - (1/2)) * length, ((size/2) - initState[1][1] - (1/2)) * length)
		shape("square")
		shapesize( length, length)
	
	else:
		goto( (int(size/2) - initState[1][0])*length, (int(size/2) - initState[1][1])*length)
		shape("square")
		shapesize( length, length)

	for i in range(size):
		for j in range(size):
			if( initState[0][i][j] == 1):
				up()
				if(size%2==0):
					goto( ((size/2) - i - (1/2)) * length, ((size/2) - j - (1/2)) * length)
					print(i)
					print(j)
					dot( length/2 , "blue")

				else:
					goto( (int(size/2) - i)*length, (int(size/2) - j)*length)
					dot( length/2 , "blue")
	
	



	
