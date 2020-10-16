a=str(input())
def triangle (b,h):
    s=b*h/2
    return (s)
def circle (b):
    s=3,14*b**2
    return (s)
def rectangle (b,c):
    s=b*c
    return (s)

def figure (a):
    if a=='t':
        b=int(input())
        h=int (input())
        print('s=',triangle (b,h))
    if a =='c':
        b = int(input())
        print('s=',circle(b))
    if a=='r':
        b = int(input())
        c = int(input())
        print('s=',rectangle(b, c))

figure(a)