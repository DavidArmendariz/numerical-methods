import pandas as pd

def biseccion(f,a,b,tol):
    if f(a)*f(b) > 0:
        print("Intervalo no válido")
        return
    error = 1e3; X_anterior = 0;
    n = 1; N = []; Xa = []; Xb = []; Xm = [];
    Fa = []; Fb = []; Fm = []; E = [];
    while error > tol:
        m = (a+b)/2
        X_actual = m
        error = abs(X_anterior-X_actual)
        N.append(n); Xa.append(a); Xb.append(b);
        Xm.append(m); Fa.append(f(a)); Fb.append(f(b));
        Fm.append(f(m)); E.append(error);
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        X_anterior = X_actual
        n += 1
    d = {"N":N,"Xa":Xa,"Xb":Xb,"Xm":Xm,"Fa":Fa,"Fb":Fb,"Fm":Fm,"E":E}
    TT = pd.DataFrame(d)
    TT.set_index("N",inplace=True)
    print(TT.to_string())
        