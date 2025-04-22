import sys
input = sys.stdin.read

def bellman_ford(n, edges):
    dist = [float('inf')] * (n + 1)
    dist[0] = 0  # 가상 정점 0번

    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 체크
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return True

    return False

data = input().split()
idx = 0
t = int(data[idx])
idx += 1
results = []

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx + 1])
    w = int(data[idx + 2])
    idx += 3

    edges = []

    # 도로 (양방향)
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        t = int(data[idx + 2])
        edges.append((u, v, t))
        edges.append((v, u, t))
        idx += 3

    # 웜홀 (단방향, 음수 시간)
    for _ in range(w):
        u = int(data[idx])
        v = int(data[idx + 1])
        t = int(data[idx + 2])
        edges.append((u, v, -t))
        idx += 3

    # 가상 정점 0에서 모든 정점으로 가중치 0 간선 추가
    for i in range(1, n + 1):
        edges.append((0, i, 0))

    result = "YES" if bellman_ford(n, edges) else "NO"
    results.append(result)

print("\n".join(results))
