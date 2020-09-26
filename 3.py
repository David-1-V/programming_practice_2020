import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-100, 100, 0.01)
plt.plot(x, np.log((x*x+1)*np.exp(-(np.abs(x))/10))/np.log(1+(np.tan(1/(1+np.sin(x)*np.sin(x))))))
plt.grid(True)
plt.show()