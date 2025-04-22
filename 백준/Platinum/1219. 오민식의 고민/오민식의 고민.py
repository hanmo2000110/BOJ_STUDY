import sys
input = sys.stdin.readline

def bellman_ford(n, start, end, edges, earn):
    dist = [float('inf')] * n
    dist[start] = -earn[start]

    for i in range(n - 1):
        for u, v, cost in edges:
            if dist[u] != float('inf') and dist[u] + cost - earn[v] < dist[v]:
                dist[v] = dist[u] + cost - earn[v]

    # 음수 사이클 탐색 (end까지 도달할 수 있는 사이클만)
    for i in range(n):
        for u, v, cost in edges:
            if dist[u] != float('inf') and dist[u] + cost - earn[v] < dist[v]:
                # 사이클이 end까지 갈 수 있는지 확인
                if can_reach(v, end, graph):
                    return "Gee"  # 무한 수익 가능

    if dist[end] == float('inf'):
        return "gg"  # 도달 불가
    else:
        return -dist[end]  # 음수로 바꿔놨으니 다시 양수화

# DFS로 도착지까지 갈 수 있는지 확인
def can_reach(start, end, graph):
    visited = [False] * len(graph)
    stack = [start]
    while stack:
        node = stack.pop()
        if node == end:
            return True
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
    return False


# 입력 처리
n, start, end, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))
    graph[u].append(v)

earn = list(map(int, input().split()))

print(bellman_ford(n, start, end, edges, earn))
