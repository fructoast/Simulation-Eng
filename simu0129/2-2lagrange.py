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

i = xlist[1]
y = ylist[1]
f = []
div = (i[0]-i[1])*(i[0]-i[2])*(i[0]-i[3])*(i[0]-i[4])*(i[0]-i[5])*(i[0]-i[6])*(i[0]-i[7])*(i[0]-i[8])*(i[0]-i[9])*(i[0]-i[10])
f.append(expand(y[0]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[1]-i[0])*(i[1]-i[2])*(i[1]-i[3])*(i[1]-i[4])*(i[1]-i[5])*(i[1]-i[6])*(i[1]-i[7])*(i[1]-i[8])*(i[1]-i[9])*(i[1]-i[10])
f.append(expand(y[1]*(x+i[0])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[2]-i[1])*(i[2]-i[0])*(i[2]-i[3])*(i[2]-i[4])*(i[2]-i[5])*(i[2]-i[6])*(i[2]-i[7])*(i[2]-i[8])*(i[2]-i[9])*(i[2]-i[10])
f.append(expand(y[2]*(x+i[1])*(x+i[0])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[3]-i[1])*(i[3]-i[2])*(i[3]-i[0])*(i[3]-i[4])*(i[3]-i[5])*(i[3]-i[6])*(i[3]-i[7])*(i[3]-i[8])*(i[3]-i[9])*(i[3]-i[10])
f.append(expand(y[3]*(x+i[1])*(x+i[2])*(x+i[0])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[4]-i[1])*(i[4]-i[2])*(i[4]-i[3])*(i[4]-i[0])*(i[4]-i[5])*(i[4]-i[6])*(i[4]-i[7])*(i[4]-i[8])*(i[4]-i[9])*(i[4]-i[10])
f.append(expand(y[4]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[0])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[5]-i[1])*(i[5]-i[2])*(i[5]-i[3])*(i[5]-i[4])*(i[5]-i[0])*(i[5]-i[6])*(i[5]-i[7])*(i[5]-i[8])*(i[5]-i[9])*(i[5]-i[10])
f.append(expand(y[5]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[0])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[6]-i[1])*(i[6]-i[2])*(i[6]-i[3])*(i[6]-i[4])*(i[6]-i[5])*(i[6]-i[0])*(i[6]-i[7])*(i[6]-i[8])*(i[6]-i[9])*(i[6]-i[10])
f.append(expand(y[6]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[0])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[7]-i[1])*(i[7]-i[2])*(i[7]-i[3])*(i[7]-i[4])*(i[7]-i[5])*(i[7]-i[6])*(i[7]-i[0])*(i[7]-i[8])*(i[7]-i[9])*(i[7]-i[10])
f.append(expand(y[7]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[0])*(x+i[8])*(x+i[9])*(x+i[10]) / div))
div = (i[8]-i[1])*(i[8]-i[2])*(i[8]-i[3])*(i[8]-i[4])*(i[8]-i[5])*(i[8]-i[6])*(i[8]-i[7])*(i[8]-i[0])*(i[8]-i[9])*(i[8]-i[10])
f.append(expand(y[8]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[0])*(x+i[9])*(x+i[10]) / div))
div = (i[9]-i[1])*(i[9]-i[2])*(i[9]-i[3])*(i[9]-i[4])*(i[9]-i[5])*(i[9]-i[6])*(i[9]-i[7])*(i[9]-i[8])*(i[9]-i[9])*(i[9]-i[10])
f.append(expand(y[9]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[0])*(x+i[10]) / div))
div = (i[10]-i[1])*(i[10]-i[2])*(i[10]-i[3])*(i[10]-i[4])*(i[10]-i[5])*(i[10]-i[6])*(i[10]-i[7])*(i[10]-i[8])*(i[10]-i[9])*(i[10]-i[0])
f.append(expand(y[10]*(x+i[1])*(x+i[2])*(x+i[3])*(x+i[4])*(x+i[5])*(x+i[6])*(x+i[7])*(x+i[8])*(x+i[9])*(x+i[0]) / div))
print(f)
fadd = expand(f[0]+f[1]+f[2]+f[3]+f[4]+f[5]+f[6]+f[7]+f[8]+f[9]+f[10])
print(fadd)
