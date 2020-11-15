import numpy as np
import random
a = random.randint(10, 100)
b = random.randint(10, 100)
random_matrix = np.random.random((a, b))
maximum = random_matrix.max()
summ = random_matrix.sum()
dividedonmax = np.array(random_matrix)/maximum
new_matrix = random_matrix - random_matrix.mean(axis=1, keepdims=True)
for i in range(len(random_matrix)):
    for j in range(len(random_matrix[i])):
        if random_matrix[i][j] == random_matrix.max():
            random_matrix[i][j] = -1
print(maximum)
print (summ)
print (random_matrix)