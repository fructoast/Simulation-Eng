#二分法
# x^2 - 2 = 0 の解

small = 0.0
big   = 2.0
i     = 0

while True :
    x = abs((small+big)/2)
    if   2 < x**2 :
        before = big
        big    = x
    elif x**2 < 2 :
        before = small
        small  = x
    else :
        break
    print("x"+str(i)+" : "+str(x))

    if abs(before-x) < 0.0000001 :
        break
    i = i+1
