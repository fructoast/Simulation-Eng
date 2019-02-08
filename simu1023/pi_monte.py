#coding:utf-8
import math
import random

def return_area(a,b):
    return math.sqrt(a**2+b**2)

pi = 0.0
times = 0
for i in range(1000000000000000000):
    if 1 > return_area(random.uniform(0,1),random.uniform(0,1)):
        pi += 1
    times += 1

    if times%10 == 1:
        print("pi:"+str((4*pi)/times))
