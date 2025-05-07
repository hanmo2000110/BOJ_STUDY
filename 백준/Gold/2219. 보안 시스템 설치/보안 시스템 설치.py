import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] =0
            
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                continue
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
cnt_connect = [INF]
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF:
            cnt += 1
    cnt_connect.append(cnt)

m = min(cnt_connect)
min_avg = INF
for i in range(1, n+1):
    if cnt_connect[i] == m:
        avg = sum(x for x in graph[i] if x != INF) / m
        if min_avg > avg:
            min_avg = avg
            result = i
print(result)        