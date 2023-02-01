from sys import stdin
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, 1, str(start)+" "))
    distance[start] = 0

    while q:
        dist, node, count, route = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < (distance[next[0]]):
                distance[next[0]] = cost
                routes[next[0]] = route + str(next[0]) + " "
                counts[next[0]] = count + 1
                heapq.heappush(
                    q, (cost, next[0], count+1, route + str(next[0]) + " "))


n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n+1)]
distance = [int(1e9) for _ in range(n+1)]
counts = [0 for _ in range(n+1)]
routes = ["" for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))
fr, to = map(int, input().split())

dijkstra(fr)

print(distance[to])
print(counts[to])
print(routes[to])
