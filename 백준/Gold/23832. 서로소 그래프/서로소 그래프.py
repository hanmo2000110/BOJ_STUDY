ans = 0
K = int(input())

for n in range(K+1):
    N = n
    result = N

    for i in range(2,int(N**0.5 + 1)):
        if N%i == 0 :
            # ans += result // i
            result -= result // i
            while N%i == 0:
                N /= i
                
    if N > 1 :
        result -= result // N
        # ans += result // N
    ans += int(result)

print(ans-1)