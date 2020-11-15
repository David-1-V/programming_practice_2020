import numpy as np
n=round(50*np.random.random ())
a=np.array
a=np.random.randint(2, 76, (n,n))
b=a.copy()
for i in range (0,n):
    for j in range (0,n):
        if ((a[i][j])%2)==1:
            a[i][j]=-1
print (b,a,sep='\n \n' )
