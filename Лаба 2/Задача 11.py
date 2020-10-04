import turtle
turtle.shape('turtle')
turtle.speed (3)
turtle.left(90)
n = 50
def butterfly(n):
    turtle.circle(n)
    turtle.circle(-n)
x = 1
while x <= 10:
    butterfly(n)
    n=n+10
    x=x+1