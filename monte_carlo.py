import numpy as np
def G(x):
    return np.exp(-x**2)
def monte_carlo(G,a,b,M):
    s = 0
    for i in range(M):
        s += G(a+(b-a)*np.random.uniform(0,1,1))
    return ((b-a)/M)*s[0]
