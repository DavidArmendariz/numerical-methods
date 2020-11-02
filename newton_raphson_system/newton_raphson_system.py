import numpy as np


def newton_raphson_system(F, J, x0, tol):
    x = x0
    error = 1e3
    n = 0
    while error > tol:
        dx = -np.linalg.solve(J(*x), F(*x))
        error = np.linalg.norm(dx) / np.linalg.norm(x)
        x += dx
        n += 1
    print("Iterations: ", n)
    return x