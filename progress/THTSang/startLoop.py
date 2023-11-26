from turtle import *
import turtle
from random import random

# Screen set up
setup(800, 400)
title("Race game")
speed(0)
bgcolor("black")
# welcome player
penup()
goto(-95, 0)
color("white")
write("Welcome to the game\n\n", font=("Times New Roman", 20, "bold"))
goto(0, 40)
write("Loading...", font = ("Times New Roman",15,"italic"))
pensize(5)
goto(-120, 30)
pendown()
for i in range (6):
    delay(300)
    forward(50)
    
# Get into the game
delay(0)
penup()
goto(-900, 700)
pendown()
begin_fill()
color("chocolate")
for i in range (2):
    forward(10000)
    right(90)
    forward(10000)
    right(90)
end_fill()
# main loop


turtle.done()
