import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))           # 정방향
    reverse_graph[v].append((u, w))   # 역방향

def dijkstra(start, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heappop(heap)
        if dist[now] < cost:
            continue
        for to, weight in graph[now]:
            if dist[to] > cost + weight:
                dist[to] = cost + weight
                heappush(heap, (dist[to], to))
    return dist

go = dijkstra(x, graph)         # X → i
back = dijkstra(x, reverse_graph)  # i → X

# 각 학생 i의 왕복 시간: i → X + X → i
answer = max(go[i] + back[i] for i in range(1, n + 1))
print(answer)
