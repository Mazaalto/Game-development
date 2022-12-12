""" A turtle race game to teach my godson coding
Checking out the project, so that it isn't too hard for six years old
Idea is to make a turlte race game, where one needs to pick a turtle that
wins the race. The turtles move at random.
The winner is the one that gets the furthest in 100 turns.

If you want to try this project out with a child, here is the link: https://projects.raspberrypi.org/en/projects/turtle-race/4
"""
from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for i in range(15):
    write(i, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

eliot = Turtle()
eliot.color('blue')
eliot.shape('turtle')

eliot.penup()
eliot.goto(-160, 100)
eliot.pendown()

matias = Turtle()
matias.color('green')
matias.shape('turtle')

matias.penup()
matias.goto(-160, 70)
matias.pendown()

aku = Turtle()
aku.color('black')
aku.shape('turtle')


aku.penup()
aku.goto(-160, 50)
aku.pendown()

for turn in range(100):
    eliot.forward(randint(1,5))
    matias.forward(randint(1,5))
    aku.forward(randint(1,5))

for turn in range(10):
    eliot.right(36)
    matias.right(36)
    aku.left(36)
