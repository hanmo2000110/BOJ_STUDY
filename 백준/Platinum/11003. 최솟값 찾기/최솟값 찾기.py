from heapq import heappush, heappop
N, L = map(int, input().split())
nums = [0] + list(map(int, input().split()))
pq = []
for i in range(1, N+1):
    heappush(pq, (nums[i], i))
    value, index = pq[0]
    while 1 <= index < i - L + 1:
        heappop(pq)
        value, index = pq[0]
    print(value, end=' ')