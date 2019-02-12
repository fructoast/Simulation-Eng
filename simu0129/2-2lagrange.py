import numpy as np
import matplotlib.pyplot as plt
from sympy import *
def func(x):
    return (1+25*x*x)**(-1)

xpoint = [5,11,21]
xlist = []
ylist = []
for points in xpoint:
    x = np.linspace(-1,1,points)
    xlist.append(x)
    y = []
    for i in x:
        y.append(func(i))
    ylist.append(y)
    #print(points,"points:\n",y)

x = Symbol('x')
i = xlist[0]
f = []
div = (i[0]-i[1])*(i[0]-i[2])*(i[0]-i[3])*(i[0]-i[4])
f.append(expand(ylist[0][0]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4]) / div))
div = (i[1]-i[0])*(i[1]-i[2])*(i[1]-i[3])*(i[1]-i[4])
f.append(expand(ylist[0][1]*(x+i[0])*(x+i[2])*(x+i[3])*(x+i[4]) / div))
div = (i[2]-i[1])*(i[2]-i[0])*(i[2]-i[3])*(i[2]-i[4])
f.append(expand(ylist[0][2]*(x+i[1])*(x+i[0])*(x+i[3])*(x+i[4]) / div))
div = (i[3]-i[1])*(i[3]-i[2])*(i[3]-i[0])*(i[3]-i[4])
f.append(expand(ylist[0][3]*(x+i[1])*(x+i[2])*(x+i[0])*(x+i[4]) / div))
div = (i[4]-i[1])*(i[4]-i[2])*(i[4]-i[3])*(i[4]-i[1])
f.append(expand(ylist[0][4]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[0]) / div))
fadd = expand(f[0]+f[1]+f[2]+f[3]+f[4])
print(fadd)

fadd = 3.32419687592101*x*x*x*x - 0.00854700854700856*x*x*x - 4.27932508104922*x*x + 0.00213675213675213*x + 1.0
plt.plot(xlist[0],fadd)
plt.show()
