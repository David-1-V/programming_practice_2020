v=float(input())
t=float(input())
if v>0:
    r=((v*t)%(109))
else:
    r=109-((abs(v*t)%109))
if (r>=109):
    r=0
print (r)