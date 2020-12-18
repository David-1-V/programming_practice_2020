import turtle as t

vx = 2
vy = 8
x = 0
y = 0
t.shape('circle')
for i in range(500):
    vy += - 0.2
    if y <= 0:
        vy = 0.75 * abs(vy)
    x += vx
    y += vy - 0.1
    t.goto(x, y)
    t.speed((vx ** 2 + vy ** 2) ** 0.5)
