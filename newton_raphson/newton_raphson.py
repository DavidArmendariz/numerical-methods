import numpy as np


def newton_raphson(f, df, xi, tol):
    x = xi
    error = 1e3
    n = 1
    while error > tol:
        x = x - f(x) / df(x)
        error = abs(f(x))
        n += 1
    print("Approximate solution: {:.4f}".format(x))
    print("Number of iterations: {:d}".format(n))
