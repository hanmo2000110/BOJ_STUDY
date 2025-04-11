import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = []
heapq.heappush(q, (0, 1))  # (비용, 노드)
heapq.heappush(dist[1], 0)

while q:
    cost, now = heapq.heappop(q)
    
    for next_node, next_cost in graph[now]:
        total_cost = cost + next_cost
        
        if len(dist[next_node]) < k:
            heapq.heappush(dist[next_node], -total_cost)
            heapq.heappush(q, (total_cost, next_node))
        elif -dist[next_node][0] > total_cost:
            heapq.heappop(dist[next_node])
            heapq.heappush(dist[next_node], -total_cost)
            heapq.heappush(q, (total_cost, next_node))

for i in range(1, n + 1):
    if len(dist[i]) < k:
        print(-1)
    else:
        print(-heapq.heappop(dist[i]))
