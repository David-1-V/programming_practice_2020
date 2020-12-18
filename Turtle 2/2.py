import turtle
turtle.color ('blue')

def number(A, delta):
    delta2 = delta + 15
    turtle.penup()
    turtle.goto(A[0][0] + delta, A[0][1])
    turtle.pendown()
    for i in range(len(A) - 1):
        turtle.goto(A[i + 1][0] + delta, A[i + 1][1])
    return delta2


x = 0
y = 0
coords = [(x, y), (x + 10, y), (x, y - 10), (x + 10, y - 10), (x, y - 20), (x + 10, y - 20)]
unus = [coords[2], coords[1], coords[5]]
quattuor = [coords[0], coords[2], coords[3], coords[5], coords[1]]
septem = [coords[0], coords[1], coords[2], coords[4]]
nihil = [coords[0], coords[1], coords[5], coords[4], coords[0]]

turtle.shape('turtle')
turtle.speed(1)
S = [unus, quattuor, unus, septem, nihil, nihil]
delta = 0

for i in range(6):
    number(S[i], delta)
    delta = number(S[i], delta)


def coords_to_file():
    f = open("turtlecoords.txt", 'w')
    res = ""
    for i in range(len(S)):
        res += str(i) + "\n"
        for coord in S[i]:
            res += str(coord[0]) + " " + str(coord[1]) + "\n"
    res += '6'
    f.write(res)
    f.close()


coords_to_file()