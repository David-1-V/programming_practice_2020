import numpy as np
n=int(input())
a=np.array
a=np.ones((n, n))
def chess (n):
    for i in range (0,n):
        for j in range (0,n):
            if ((i+j)%2)==0:
                a[i][j]=0
    print (a)
chess (n)