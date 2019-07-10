def hanoi(n,pivote_inicial,pivote_final,pivote_auxiliar):
    if n==1:
        print(pivote_inicial+"->"+pivote_final)
    else:
        hanoi(n-1,pivote_inicial,pivote_auxiliar,pivote_final)
        print(pivote_inicial+"->"+pivote_final)
        hanoi(n-1,pivote_auxiliar,pivote_final,pivote_inicial)
        
        
