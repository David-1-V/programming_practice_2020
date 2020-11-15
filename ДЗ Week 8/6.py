import numpy as np
a=np.array
k=round(10*np.random.random ())
f=round(10*np.random.random ())
a=np.random.randint(0, 100, (k,f))
def n (a):
    a=(a/(max(abs(np.max(a)), abs(np.min(a)))))
    return a
a=n(a)
print (a)