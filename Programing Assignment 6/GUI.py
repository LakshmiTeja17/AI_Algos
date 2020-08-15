#NAME: J LAKSHI TEJA
#ID: 2017A7PS0068P

from turtle import *
from random import *
from math import *
import turtle


def filled_rectangle(t, l, w):
    t.begin_fill()
    for i in range(2):
        t.right(90)
        t.forward(l)
        t.right(90)
        t.forward(w)
    t.end_fill()

def display_block(t, s, row, col):
    t.setpos(col+0.5, 9-row)
    if s.mat[col-1][row-1] == 1:
        t.color("blue", "blue")
    if s.mat[col-1][row-1] == 0:
        t.color("green", "green")
    t.begin_fill()
    t.circle(0.5)
    t.end_fill()
    t.color("white")
    t.setpos(col+0.5,9-row+0.1)
    t.begin_fill()
    t.circle(0.4)
    t.end_fill()

    

    if s.mat[col-1][row-1] == 1:
        t.color("blue", "blue")
    if s.mat[col-1][row-1] == 0:
        t.color("green", "green")
    t.setpos(col+0.5,9-row+0.2)

    t.begin_fill()
    t.circle(0.3)
    t.end_fill()
    t.color("black")

def initialize(t):
    turtle.tracer(0)
    t.pensize(1.5)
    t.penup()
    boxes(t)

def changetogreen(t,y,x,listed):
    t.setpos(23+(x-1)*25,85-(y-1)*10)
    t.color("green")
    filled_rectangle(t,5,16)
    t.color("red")
    t.setpos(14+25*(x-1),79-(y-1)*10)
    ch=""
    if x%2==0:
        ch="~"
    t.write(ch + listed[y-1], True, align="center", font=("Arial", 12, "normal"))

def clicked(t,x,y,listed):
    changetogreen(t,x,y,listed)



def boxes(t):
#    query and condition boxes 
    t.color("white")
    t.setpos(45,95)
    filled_rectangle(t,5,40)
    t.setpos(25,89)
    t.color("blue")
    t.write("Query Variables", True, align="center", font=("Arial", 12, "normal"))
    t.setpos(95,95)
    t.color("white")
    filled_rectangle(t,5,40)
    t.setpos(75,89)
    t.color("blue")
    t.write("Condition Variables", True, align="center", font=("Arial", 12, "normal"))

#   generate box
    
    t.setpos(80,-70)
    t.color("yellow")
    filled_rectangle(t,10,60)
    t.setpos(50,-78)
    t.color("blue")
    t.write("Evaluate", True, align="center", font=("Arial", 12, "normal"))

def list_boxes(t,list):
	l= len(list)
	count = 0
	for element in list:
		for i in range(4):
			t.color("yellow")
			t.setpos(23 + 25*i,85-count*10)
			filled_rectangle(t,5,16)
			t.color("red")
			t.setpos(14 + 25*i,79-count*10)
			if( i%2 == 0):
				t.write(element, True, align="center", font=("Arial", 12, "normal"))
			else:
				t.write('~' + element, True, align="center", font=("Arial", 12, "normal"))			

		count=count+1

def displayAnswer(t,answer):
    t.color("white")
    t.setpos(90,-85)
    filled_rectangle(t,10,80)
    t.setpos(45,-94)
    t.color("blue")
    t.write("Answer: "+str(answer), True, align="center", font=("Arial", 20, "normal"))

def initialize_board():
    # Invoking the screen and setting the window size.
    screen = Screen()
    screen.bgcolor("white")
    screen.title("Bayesian Network")
    screen.setworldcoordinates(0, -100, 100, 100)

    # screen.screensize(canvwidth=200, canvheight=200, bg=None)
    t = Turtle()
    #t.ht()
    t.speed(0)
    initialize(t)

    return screen, t
