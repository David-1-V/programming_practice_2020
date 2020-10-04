import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
x = 1
def circle (x):
    while x <= 6:
        turtle.circle(-50, 180, 50)
        turtle.circle(-10, 180, 50)
        x=x+1
circle(x)