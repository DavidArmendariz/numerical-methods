function x = newton(f,df,xi,tol)
x = xi;
error = 1e3;
n = 1;
while error > tol
    x = x - f(x)/df(x);
    error = abs(f(x));
    n = n+1;
end
fprintf("Numero de iteraciones: %d",n)