import numpy as np
import matplotlib.pyplot as plt

def out(n,pn):
    x_n = np.linspace(-1,1,n)
    y_n = (1+25*x_n**2) ** (-1)
    k = len(x_n) - 1

    def l(j,x):
        y = 1
        for m in range (k + 1):
            if(m != j):
                y *= (x-x_n[m]) / (x_n[j]-x_n[m])
        return y

    def L(x):
        lx = 0
        for j in range (k+1):
            lx += y_n[j] * l(j,x)
        return lx

    x=np.linspace(-1,1,50)
    y = x * 0
    for index,i in enumerate(x):
        y[index] = L(i)
    plt.subplot(2,2,pn)
    plt.plot(x,y)
    plt.plot(x_n,y_n,"x")
out(5,1)
out(11,2)
out(21,3)
plt.show()
