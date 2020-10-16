a = int(input())
b = int(input())
def nod (a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return (a)
print (nod(a,b))
