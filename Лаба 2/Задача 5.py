import turtle

turtle.shape('turtle')
for i in range (10):
    turtle.forward(250-20*i)
    turtle.left(90)
    turtle.forward(250-20*i)
    turtle.left(90)
    turtle.forward(250-20*i)
    turtle.left(90)
    turtle.forward(250-20*i)
    turtle.left(90)
    turtle.penup()
    turtle.goto(10 * (i+1), 10 * (i+1))
    turtle.pendown()
