def secant(f, x1, x2, tol):
    error = 1e3
    n = 0
    x3 = 0
    while error > tol:
        x3 = x1 - ((x2 - x1) / (f(x2) - f(x1))) * f(x1)
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        n += 1
    print("Approximate solution: {:.4f}".format(x3))
    print("Number of iterations: {:d}".format(n))
