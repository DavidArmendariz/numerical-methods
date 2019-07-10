function [coef] = interpolacion_trigonometrica(x,y)
%length(x) = 2n+1
n = (length(x)-1)/2;
A = ones(2*n+1,2*n+1);
for i=1:2*n+1
    k=1;
    for j=2:n+1
        A(i,j) = cos(k*x(i));
        k=k+1;
    end
    k=1;
    for j=n+2:2*n+1
        A(i,j) = sin(k*x(i));
        k=k+1;
    end
end
coef = A\y';
xd = linspace(x(1),x(end));
yd = [];
for i=1:length(xd)
    s = coef(1);
    for k=1:n
        s = s+coef(k+1)*cos(k*xd(i));
        s = s+coef(k+n+1)*sin(k*xd(i));
    end
    yd = [yd,s];
end
plot(x,y,'*',xd,yd)