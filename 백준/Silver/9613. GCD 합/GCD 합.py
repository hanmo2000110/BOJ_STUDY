import math 

n = int(input())

for _ in range(n):
    result = 0
    arr = list(map(int,input().split()))
    for i in range(arr[0]):
        for j in range(i+1,arr[0]):
            result += math.gcd(arr[1+i],arr[1+j])
    print(result)