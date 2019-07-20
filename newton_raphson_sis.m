function [x] = newton_raphson_sis(F,J,x0,tol)
x=x0;
error=1e3;
n=0;
while error > tol
    dx = -J(x)\F(x);
    error = norm(dx)/norm(x);
    x = x+dx;
    n = n+1;
end
fprintf("Iteraciones: %d",n)