import sys
input = sys.stdin.readline
 
INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    # 최단 경로 행렬 초기화
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]

    # 동적 프로그래밍을 통한 갱신
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# 예시 그래프


n = int(input())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
while True :
    a,b = map(int, input().split())
    if a == -1 and b == -1 :
        break
    graph[a][a] = 0
    graph[b][b] = 0
    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)

shortest_paths = floyd_warshall(graph)
values = []
result = []

# print("최단 경로 행렬:")
for row in shortest_paths[1:]:
    values.append(max(row[1:]))
    
m = min(values)

for i in range(n):
    if values[i] == m :
        result.append((i+1))

print(m,values.count(m))
print(" ".join(map(str,sorted(result))))


