import numpy as np
from numpy import loadtxt
x = np.arange(2, 75, 1)
np.savetxt('1.dat', x, delimiter=',')
lines = loadtxt("1.dat", delimiter=",")
print(lines)