def eratostenes(n):
    primos = [True for i in range(n+1)]
    #primos[0] = False
    #primos[1] = False
    for m in range(2,n+1):
        k = 2
        while m*k <= n:
            primos[m*k] = False
            k += 1
    for m in range(2,n+1):
        if primos[m] == True:
            print(m)
        
