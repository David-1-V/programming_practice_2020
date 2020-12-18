import turtle


def reading_coords(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    res = []
    coords_for_number = []
    for line in lines:
        line = line.strip()
        if len(line) == 1:
            wow = int(line)
            if wow != 0:
                res.append(list(coords_for_number))
                coords_for_number = []
        else:
            coords_for_number.append([int(x) for x in line.split()])
    return res


def number(A, delta):
    delta2 = delta + 15
    turtle.penup()
    turtle.goto(A[0][0] + delta, A[0][1])
    turtle.pendown()
    for i in range(len(A) - 1):
        turtle.goto(A[i + 1][0] + delta, A[i + 1][1])
    return delta2


turtle.shape('turtle')
turtle.speed(1)
S = reading_coords('turtlecoords.txt')
delta = 0
for i in range(6):
    number(S[i], delta)
    delta = number(S[i], delta)
