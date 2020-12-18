from random import randint
from random import random
import turtle

number_of_turtles = 10
steps_of_time_number = 500
turtle.mode("logo")

turtle.ht()
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.goto(-100, 100)
turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(-100, -100)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-95, 95), randint(-95, 95))
    unit.right(360 * random())
    unit.shapesize(0.6, 0.6, 0.6)

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(1)
        for i in range(number_of_turtles):
            if abs(pool[i].xcor() + 100) <= 5 or abs(pool[i].xcor() - 100) <= 5:
                pool[i].seth(-pool[i].heading())
                pool[i].forward(1)

            if abs(pool[i].ycor() + 100) <= 5 or abs(pool[i].ycor() - 100) <= 5:
                pool[i].seth(pool[i].heading() - 180)
                pool[i].forward(1)

            for j in range(number_of_turtles):
                if i != j and abs(pool[i].xcor() - pool[j].xcor()) <= 5 and abs(pool[i].ycor() - pool[j].ycor()) <= 5:
                    k = pool[i].heading()
                    pool[i].setheading(pool[j].heading())
                    pool[j].setheading(k)
                    pool[i].forward(1)
                    pool[j].forward(1)
