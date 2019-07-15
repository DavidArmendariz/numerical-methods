function [] = runge_kutta_sis(f,g,x0,y0,a,b,h)
t = a:h:b; n = length(t);
x = [x0]; y = [y0];
for i=1:n-1
    k1 = h*f(x(i),y(i),t(i));
    l1 = h*g(x(i),y(i),t(i));
    k2 = h*f(x(i)+k1/2,y(i)+l1/2,t(i)+h/2);
    l2 = h*g(x(i)+k1/2,y(i)+l1/2,t(i)+h/2);
    k3 = h*f(x(i)+k2/2,y(i)+l2/2,t(i)+h/2);
    l3 = h*g(x(i)+k2/2,y(i)+l2/2,t(i)+h/2);
    k4 = h*f(x(i)+k3,y(i)+l3,t(i)+h);
    l4 = h*g(x(i)+k3,y(i)+l3,t(i)+h);
    x(i+1) = x(i)+(1/6)*(k1+2*k2+2*k3+k4);
    y(i+1) = y(i)+(1/6)*(l1+2*l2+2*l3+l4);
end
plot(t,x,t,y)