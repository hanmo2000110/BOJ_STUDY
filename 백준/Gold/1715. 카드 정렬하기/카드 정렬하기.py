from collections import deque
from heapq import heappush, heappop

n = int(input())
l = []
for i in range(n):
    heappush(l, int(input()))

if n == 1:
    print(0)
    exit()
count = 0
while True:
    a = heappop(l)
    b = heappop(l)
    s = a + b
    count += s
    if len(l) == 0:
        print(count)
        break
    heappush(l, s)