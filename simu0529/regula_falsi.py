#はさみうち法
# f(x) = 3tan^(-1)(x-1)+x/4 = 0 の解
import math

def fanc(x):
    return 3 * math.atan(x-1) + x / 4

if __name__ == '__main__':
    small = 0.0
    big   = 2.5
    i     = 0

    while True :
        fanc_s    = 3 * math.atan(small)
        fanc_b    =        big**2 - 2
        gradient_x = (fanc_b*small - fanc_s*big)/(fanc_b - fanc_s)

        fanc_grax = gradient_x**2 - 2
        if  fanc_grax*fanc_s <= 0 :
            #next_small = small
            before      = big
            big         = gradient_x
        else :
            before      = small
            small       = gradient_x
            #next_big   = big

        print("x"+str(i)+" : "+str(gradient_x))
        i = i + 1
        
        if abs(before-gradient_x) < 0.0000001 :
            break

        
