#encode:utf-8
import math

def trapezoid_integral(a,b,power):
    n = 10000 #n=サンプリング数,任意の数
    h = (b-a)/n
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
    result = add * h / 2
    print("trapezoid:",result)

def simpson_integral(a,b,power):
    n = 10000 #n=サンプリング数,任意の数
    n *= 2
    h = (b-a)/n
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
                if term%2 == 1:
                    add += 4*level3_func(h*term)
                else:
                    add += 2*level3_func(h*term)
            elif power==4:
                if term%2 == 1:
                    add += 2*level4_func(h*term)
                else:
                    add += 2*level4_func(h*term)
            else:
                print("undefined.")
    result = add * h / 3
    print("simpson:",result)

def level3_func(x):
    return float(4*x**3-10*x**2+4*x+5)

def level4_func(x):
    return float(x**4+2*x)

#~0-2(4x^3-10x^2+4x+5)dx
trapezoid_integral(0,2,3)
simpson_integral(0,2,3)
#~0-3(x^4+2x)dx
trapezoid_integral(0,3,4)
simpson_integral(0,3,4)
