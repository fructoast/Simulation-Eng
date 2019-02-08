#ニュートン法
# f(x) = x^2 - 2 = 0 の解
#f'(x) = 2x      = 0

x   = 2.0
i   = 0

print("x0 : "+str(x))
while True:
    fanc_x = x**2 - 2
    differentiated = 2 * x #differentiated -> 微分された
    next_x = x - fanc_x/differentiated

    print("x"+str(i+1)+" : "+str(next_x))

    if abs(next_x-x) < 0.0000001 :
        break
    x = next_x
    i = i+1
