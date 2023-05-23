INT_SETUP=150
SPEED=0
BOX_LENGTH=300

#import and intial set up
import turtle
turtle.setup(600,600)
turtle.speed(SPEED)

#Pen up to get to start point
turtle.penup()
turtle.forward(INT_SETUP)
turtle.left(90)
turtle.forward(INT_SETUP)
turtle.pendown()

#change the way turtle faces to start
turtle.left(90)

#Create range of the boxes
#draw box with 95 degree turns to create design
for j in range(20):
    for i in range(4):
        turtle.forward(BOX_LENGTH)
        turtle.left(95)
        
