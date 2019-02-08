x = 0
y = 0
z = 0

for i in range(50):
    if(i%10==0):
        print(i)
    print(x,y,z)
    x = (10-y-z)/5
    y = (12-x-z)/4
    z = (13-y-2*x)/3
