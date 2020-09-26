import numpy as np
x= [1, 10, 1000]
for i in x:
    y = np.log((1 / (np.exp(np.sin(i) + 1))) / (5 / 4 + 1 / (i ** 15))) / np.log(i* i + 1)
    print (y)
