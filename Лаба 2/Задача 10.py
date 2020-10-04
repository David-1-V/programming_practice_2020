import turtle
turtle.shape('turtle')
turtle.speed=1
n = 8
x = 1
def flower(x):
    while x <= n:
        turtle.circle(50)
        turtle.left(360 / n)
        x=x+1
flower (x)
