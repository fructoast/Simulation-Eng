#encode:utf-8
import math

def trapezoid_integral(a,b,power):
    n = 100 #n=任意の数
    h = (b-a)/2*n
    add = 0
    for term in range(n+1):
        if term==0 or term==n:
            if power==3:
                add += level3_func(h*term)
            elif power==4:
                add += level4_func(h*term)
            else:
                print("undefined.")
        else:
            if power==3:
                add += 2*level3_func(h*term)
            elif power==4:
                add += 2*level4_func(h*term)
            else:
                print("undefined.")
    result = add * h

    print("leve3-result:",result)


def level3_func(x):
    return float(4*x**3-10*x**2+4*x+5)

def level4_func(x):
    return float(x**4+2*x)

#~0-2(4x^3-10x^2+4x+5)dx
trapezoid_integral(0,2,3)
#~0-3(x^4+2x)dx
trapezoid_integral(0,3,4)
