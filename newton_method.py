import numpy as np

def newton(f,df,xi,tol):
    x = xi
    error = 1e3
    n = 1
    while error > tol:
        x = x-f(x)/df(x)
        error = abs(f(x))
        n += 1
    print("Solucion aproximada: {:.4f}".format(x))
    print("Numero de iteraciones: {:d}".format(n))
