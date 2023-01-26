'''
철로 골2
https://www.acmicpc.net/problem/13334
- 자료 구조
- 정렬
- 스위핑
- 우선순위 큐

접근법 :
h와 o의 범위가 너무 넓기 때문에 이중 반복문을 사용해선 안되며
스위핑 기법으로 풀어야 한다는데 그러기 위해선 정렬을 해야할것 같다
정렬 기준이 문제인데 

스위핑 :
스위핑이라는 건 그냥 어떤 선이나 공간을 한쪽에서부터 싹 쓸어버린다는 건데
한 번만 전체 공간을 스캔하면서 마주치는 요소들에 대해 뭔가를 해 주면 정답이 구해지는 형태입니다.

'''
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
