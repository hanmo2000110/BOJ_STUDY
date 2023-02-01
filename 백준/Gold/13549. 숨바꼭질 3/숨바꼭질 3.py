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
        t = []
        if node - 1 >= 0:
            t.append((1, node-1))

        if node + 1 < 100001:
            t.append((1, node+1))

        if node*2 < 100001:
            t.append((0, node*2))

        for next in t:
            cost = distance[node] + next[0]
            # print(next[1])
            if cost < (distance[next[1]]):
                distance[next[1]] = cost
                # routes[next[1]] = route + str(next[1]) + " "

                heapq.heappush(
                    q, (cost, next[1]))


n, k = map(int, stdin.readline().split())
distance = [int(1e9) for _ in range(100001)]
# routes = ["" for _ in range(100001)]
dijkstra(n)

print(distance[k])
# print(routes[k])
