N = int(input())
result = N

for i in range(2,int(N**0.5 + 1)):
    if N%i == 0 :
        result -= result // i
        while N%i == 0:
            N /= i
            
if N > 1 :
    result -= result // N
    
print(int(result))