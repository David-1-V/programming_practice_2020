import turtle
turtle.shape('turtle')
turtle.speed (1)
n = int(input())
def stars(n):
    turtle.left(180 - (180 / n))
    turtle.forward(200)
x = 1
while x <= n:
    stars(n)
    x=x+1
