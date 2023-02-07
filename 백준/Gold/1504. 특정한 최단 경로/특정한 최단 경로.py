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


n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [1e9 for _ in range(n+1)]
result = [[], []]
for _ in range(e):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())

dijkstra(1)
# print(distance)
if distance[n] == 1e9:
    print(-1)
else:
    result[0].append(distance[v1])
    result[1].append(distance[v2])
    distance = [1e9 for _ in range(n+1)]
    dijkstra(v1)
    # print(distance)

    result[0].append(distance[v2])
    result[1].append(distance[n])
    distance = [1e9 for _ in range(n+1)]
    dijkstra(v2)
    # print(distance)
    result[0].append(distance[n])
    result[1].append(distance[v1])

    # print(result)

    t = min(sum(result[0]), sum(result[1]))

    if t >= 1e9:
        print(-1)
    else:
        print(t)
