import sys
input = sys.stdin.readline
 
INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    # 최단 경로 행렬 초기화
    # 0 if i == j else
    dist = [[ graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
 
    # 동적 프로그래밍을 통한 갱신
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# 예시 그래프


v,e = map(int, input().split())
graph = [[INF for _ in range(v+1)] for _ in range(v+1)]

for i in range(e) :
    a,b,c = map(int, input().split())
    
    graph[a][a] = 0
    graph[b][b] = 0
    graph[a][b] = c

# print(graph)

shortest_paths = floyd_warshall(graph)

path = []
# print("최단 경로 행렬:")
for row in shortest_paths[1:]:
    path.append(row[1:])
    
result = INF

for i in range(v) :
    # print(path[i][i])
    if path[i][i] == INF :
        continue
    result = min(result,path[i][i])

if result == INF : 
    print(-1)
else :
    print(result)
    

