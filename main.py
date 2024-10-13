import random
import turtle
from turtle import Turtle
t = Turtle()
turtle.colormode(255)
s = turtle.Screen()
user_choice = s.textinput(title="Make your bet", prompt="Which turtle will win(red/blue/green)").lower().replace("",'')
start_race = True
t.speed(0)
s.setup(width=500,height=400)
racers = []
color = ['red','blue','green','yellow']
for i in range(4):
    tim = Turtle(shape='turtle')
    racers.append(tim)
    tim.color(color[i])
    tim.penup()
    tim.goto(-230, i*30)
winner = racers[0]
while start_race:
    for i in range(4):
        if(racers[i].xcor()) > 230:
            start_race = False
            winner = racers[i].pencolor()
            print(user_choice)
            print(winner)
        racers[i].forward(random.randint(1, 10))

if(winner == user_choice):
    print("you Won")
else:
    print("you lost")

def Right():
    t.setheading(0)
    t.forward(40)


def Up():
    t.setheading(90)
    t.forward(40)


def Left():
    t.setheading(180)
    t.forward(40)


def Down():
    t.setheading(270)
    t.forward(40)


s.listen()
s.onkey(key='Up', fun=Up)
s.onkey(key='Down', fun=Down)
s.onkey(key='Right', fun=Right)
s.onkey(key='Left', fun=Left)

s.exitonclick()
