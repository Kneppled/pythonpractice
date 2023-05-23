#Creating pentagon design
import turtle
turtle.setup(600,600) #Size of turtle window
turtle.penup()  #Get to starting location
turtle.speed(0) #set speed to fastest to create design
turtle.goto(200,0) #Starting location
turtle.pendown()    #Start drawing design

#Create pentagon image
turtle.goto(150,-250) 
turtle.goto(-150,-250)
turtle.goto(-200,0)
turtle.goto(200,0)
turtle.goto(0,150)
turtle.goto(-200,0)
turtle.goto(150,-250)
turtle.goto(0,150)
turtle.goto(-150,-250)
turtle.goto(200,0)
turtle.hideturtle() #Hide the turtle after design is completed
