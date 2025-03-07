import math

n,m = map(int, input().split())
check = [0 for _ in range(m+1)]

for i in range(2,int(math.sqrt(m))+1) :
    if check[i] == 1 :
        continue
    for j in range(i*2,m+1,i):
            check[j] = 1

for i in range(n,m+1) :
    if check[i] == 0 and i != 1:
        print(i)


