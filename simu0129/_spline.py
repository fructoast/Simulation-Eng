import numpy as np
import matplotlib.pyplot as plt
def show_graph(coef):#coefficient
    x = np.linspace(1,2,20)
    y = coef[0]*x**3+coef[1]*x**2+coef[2]*x+coef[3]
    plt.plot(x,y)
    x = np.linspace(2,3,20)
    y = coef[4]*x**3+coef[5]*x**2+coef[6]*x+coef[7]
    plt.plot(x,y)
    x = np.linspace(3,4,20)
    y = coef[8]*x**3+coef[9]*x**2+coef[10]*x+coef[11]
    plt.plot(x,y)
    plt.show()
    
A = np.array([[ 1,1,1,1,  0, 0, 0,0,  0, 0, 0,0],
              [ 8,4,2,1,  0, 0, 0,0,  0, 0, 0,0],
              [ 0,0,0,0,  8, 4, 2,1,  0, 0, 0,0],
              [ 0,0,0,0, 27, 9, 3,1,  0, 0, 0,0],
              [ 0,0,0,0,  0, 0, 0,0, 27, 9, 3,1],
              [ 0,0,0,0,  0, 0, 0,0, 64,16, 4,1],
              [12,4,1,0,-12,-4,-1,0,  0, 0, 0,0],
              [12,2,0,0,-12,-2, 0,0,  0, 0, 0,0],
              [ 0,0,0,0, 27, 6, 1,0,-27,-6,-1,0],
              [ 0,0,0,0, 18, 2, 0,0,-18,-2, 0,0],
              [ 6,2,0,0,  0, 0, 0,0,  0, 0, 0,0],
              [ 0,0,0,0,  0, 0, 0,0, 24, 6, 0,0]])
B = np.array([9,4,4,6,6,3,0,0,0,0,0,0])
X = np.linalg.solve(A,B)
ans = [X[0:4],X[4:8],X[8:12]]
for func in ans:
    print(func[0],"x^3 + ",func[1],"x^2 + ",func[2],"x + ",X[3])
show_graph(X)
