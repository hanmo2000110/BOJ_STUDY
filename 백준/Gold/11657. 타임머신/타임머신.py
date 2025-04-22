def bellman_ford(n, edges, start):
    dist = [float('inf')] * n
    dist[start] = 0

    # 정점 수 - 1번 반복
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 체크
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # 음수 사이클 존재

    return dist

n,m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
ans = bellman_ford(n+1,edges,1)

if ans == None:
    print(-1)
else :
    for i in range(2,len(ans)):
        if ans[i] == float('inf'):
            print(-1)
        else :
            print(ans[i])
        
