from sys import stdin
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < (distance[next[0]]):
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


v, e = map(int, stdin.readline().split())
k = int(stdin.readline())
graph = [[] for _ in range(v+1)]
distance = [int(1e9) for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, len(distance)):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
