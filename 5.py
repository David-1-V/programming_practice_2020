import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
a = np.arange(0, 10, 0.01)
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
c, d= np.polyfit(x, y, deg=2, cov=True)
e, h= np.polyfit(x, y, deg=3, cov=True)
p_f = np.poly1d(p)
c_f = np.poly1d(c)
e_f = np.poly1d(e)
plt.errorbar(x, y, xerr=0.05, yerr=0.08)
plt.plot(a,p_f(a))
plt.plot(a, c_f(a))
plt.plot (a,e_f(a))
plt.grid(True)
plt.show()

