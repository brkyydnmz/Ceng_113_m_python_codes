import turtle   
import time
import random


print ("This program draws shapes based on the number you enter.")
num_str = input("Enter the side number of the shape : ")
if num_str.isdigit():
    squares = int(num_str)
else:
    print("PLEASE PRESS NUMBER!")


angle = 180 - 180*(squares-2)/squares
x = 0
y = 0
turtle.setpos(x, y) #start position


numshapes = 15   #figure drawn 15 times
for x in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())  # for random colors (every shape)
    x =x+10  # or x+=10
    y=y+10 #or y+=10
    turtle.forward(x)
    turtle.right(y) 
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(100)
        turtle.left(angle) #turn left with angle degree
        turtle.forward(100)
        print (turtle.pos())  # turtle.pos = turtle's position
        turtle.up()
        turtle.end_fill()

turtle.bye()


