import turtle
turtle.shape('turtle')
turtle.speed (1)
def right (n,dlina):
    angle=((180*(n-2))/n)
    for i in range (n):
        turtle.forward(dlina)
        turtle.left(180-angle)

for i in range (3,11):
    right (i,50+20*i)
    turtle.penup()
    turtle. goto (-5*i,-5*i)
    turtle. pendown ()
