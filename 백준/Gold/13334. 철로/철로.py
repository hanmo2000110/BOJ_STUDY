import sys
import heapq

n = int(input())
l = []
heap = []
temp = []
result = 0
for _ in range(n):
    temp.append(list(map(int, sys.stdin.readline().split())))
d = int(input())

for x in temp:
    h, o = x
    if abs(h - o) <= d:
        x = sorted(x)
        l.append(x)

l = sorted(l, key=lambda x: -x[1])
# print(l)
while l:
    t = l.pop()
    while heap and heap[0][0] < t[1] - d:
        heapq.heappop(heap)
    heapq.heappush(heap, t)

    result = max(result, len(heap))

print(result)