import math

N,L = map(int, input().split())
holes = []
for i in range(N):
    holes.append(tuple(map(int, input().split())))

holes.sort()

k = 0
ans = 0
for hole in holes :
    start, end = hole
    if k > start :
        start = k
    if end > k :
        k = end

    c = math.ceil((end-start)/L)
    ans += c
    k = start + c * L

print(ans)