import numpy as np
import matplotlib.pyplot as plt

def interpolacion_trigonometrica(x,y):
    n = int((len(x)-1)/2)
    x = np.array(x)
    y = np.array(y)
    A = np.ones((2*n+1,2*n+1))
    for i in range(2*n+1):
        k=1
        for j in range(1,n+1):
            A[i,j] = np.cos(k*x[i])
            k += 1
        k=1
        for j in range(n+1,2*n+1):
            A[i,j] = np.sin(k*x[i])
            k += 1
    coef = np.linalg.solve(A,y)
    xd = np.linspace(x[0],x[-1])
    yd = []
    for i in range(len(xd)):
        s = coef[0]
        for k in range(1,n+1):
            s += coef[k]*np.cos(k*xd[i])
            s += coef[k+n]*np.sin(k*xd[i])
        yd.append(s)
    yd = np.array(yd)
    plt.plot(x,y,'*',xd,yd)
    plt.show()
