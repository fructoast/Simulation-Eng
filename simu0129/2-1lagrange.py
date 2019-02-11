import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (1+25*x*x)**(-1)

xpoint = [5,11,21]
for points in xpoint:
    x = np.linspace(-1,1,points)
    y = []
    for i in x:
        y.append(func(i))
    print(points,"points:\n",y)
