G = function(x){
  return(exp(-x^2))
}
monte_carlo = function(G,a,b,M){
  s = 0
  for(i in 1:M){
    s = s + G(a+(b-a)*runif(1,0,1))
  }
  return(((b-a)/M)*s)
}