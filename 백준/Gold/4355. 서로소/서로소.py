while True:
    N = int(input())
    if N == 1:
        print(0)
        continue
    if N == 0: 
        break
    result = N

    for i in range(2,int(N**0.5 + 1)):
        if N%i == 0 :
            result -= result // i
            while N%i == 0:
                N /= i
                
    if N > 1 :
        result -= result // N
        
    print(int(result))