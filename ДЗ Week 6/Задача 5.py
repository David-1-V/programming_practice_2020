import matplotlib.pyplot as plt
def function (x):
    if -5<=i<=5:
        return (x*x)
    if i<-5:
        return (2*abs(i)-1)
    if i>5:
        return (2*i)
for i in range (-10,11,1):
    print(function(i), end=' ')
x=float()
plt. plot(x, function(x))
plt.grid(True)
plt.show()