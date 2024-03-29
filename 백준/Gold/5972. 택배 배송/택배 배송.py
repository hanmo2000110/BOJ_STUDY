import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

def Dijkstra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

distances = Dijkstra(1)
print(distances[n])