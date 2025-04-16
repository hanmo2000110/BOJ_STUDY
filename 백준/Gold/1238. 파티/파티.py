from heapq import heappop, heappush

n,m,x = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
l = [[] for _ in range(n+1)]
dijkstra = [[1000001 for _ in range(n+1)] for _ in range(n+1)]

for fr, to, value in arr:
    l[fr].append((to, value))

for i in range(1,n+1):
    dijkstra[i][i] = 0

    heap = [(0 ,i)]

    while heap:
        value, now = heappop(heap)
        if dijkstra[i][now] < value:
            continue
        dijkstra[i][now] = value
        for to, val in l[now]:
            if dijkstra[i][to] > dijkstra[i][now]+val :
                dijkstra[i][to] = dijkstra[i][now]+val
                heappush(heap, (dijkstra[i][to], to))

ans = 0
for i in range(1,n+1):
    ans = max(ans, dijkstra[x][i] + dijkstra[i][x])
    
print(ans)

