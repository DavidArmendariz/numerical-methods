function r = biseccion(f,a,b,tol)
if f(a)*f(b) > 0
    disp("Intervalo no válido")
    return
end
error = 1e3;
X_anterior = 0;
n = 1;
N = []; Xa = []; Xb = []; Xm = []; 
Fa = []; Fb = []; Fm = []; E = [];
while error > tol
    m = (a+b)/2;
    X_actual = m;
    error = abs(X_actual-X_anterior);
    N = [N;n]; Xa = [Xa;a]; Xb = [Xb;b];
    Xm = [Xm;m]; Fa = [Fa;f(a)]; Fb = [Fb;f(b)];
    Fm = [Fm;f(m)]; E = [E;error];
    if f(a)*f(m) < 0
        b = m;
    else
        a = m;
    end
    X_anterior = X_actual;
    n = n+1;
end
r = X_anterior; TT = table(N,Xa,Xb,Xm,Fa,Fb,Fm,E)