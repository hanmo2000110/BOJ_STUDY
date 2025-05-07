INF = int(1e9)

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# 입력
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
teleports = [tuple(map(int, input().split())) for _ in range(3)]

# 노드 구성
nodes = [(x1, y1), (x2, y2)]
for a, b, c, d in teleports:
    nodes.append((a, b))
    nodes.append((c, d))

n = len(nodes)

# 거리 배열 초기화 (맨해튼 거리)
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = dist(nodes[i], nodes[j])

# 텔레포트 쌍은 거리 10초와 기존 거리 중 더 짧은 것으로 설정
for i in range(3):
    a = 2 + i * 2
    b = a + 1
    graph[a][b] = graph[b][a] = min(graph[a][b], 10)

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 결과 출력 (시작점 → 도착점)
print(graph[0][1])
