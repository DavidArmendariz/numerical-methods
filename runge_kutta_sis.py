import numpy as np
import matplotlib.pyplot as plt
def runge_kutta_sis(f,g,x0,y0,a,b,h):
    t = np.arange(a,b+h,h)
    n = len(t)
    x = np.zeros(n); y = np.zeros(n);
    x[0] = x0; y[0] = y0;
    for i in range(n-1):
        k1 = h*f(x[i],y[i],t[i])
        l1 = h*g(x[i],y[i],t[i])
        k2 = h*f(x[i]+k1/2,y[i]+l1/2,t[i]+h/2)
        l2 = h*g(x[i]+k1/2,y[i]+l1/2,t[i]+h/2)
        k3 = h*f(x[i]+k2/2,y[i]+l2/2,t[i]+h/2)
        l3 = h*g(x[i]+k2/2,y[i]+l2/2,t[i]+h/2)
        k4 = h*f(x[i]+k3,y[i]+l3,t[i]+h)
        l4 = h*g(x[i]+k3,y[i]+l3,t[i]+h)
        x[i+1] = x[i]+(1/6)*(k1+2*k2+2*k3+2*k4)
        y[i+1] = y[i]+(1/6)*(l1+2*l2+2*l3+2*l4)
    plt.plot(t,x,t,y)
    plt.show()
        
        
        
