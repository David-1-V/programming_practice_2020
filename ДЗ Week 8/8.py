import numpy as np
def function (random_array, value):
    array = np.asarray(random_array)
    index = (np.abs(array - value)).argmin()
    return array[index]
array = np.random.random(100)
print(array)
value = 0.5
print(function(array, value))