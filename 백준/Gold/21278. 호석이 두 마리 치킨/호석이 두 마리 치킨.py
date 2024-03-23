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




n,m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(m) :
    a,b = map(int, input().split())
    
    graph[a][a] = 0
    graph[b][b] = 0
    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)

shortest_paths = floyd_warshall(graph)

# print("최단 경로 행렬:")
# for row in shortest_paths[1:]:
#     print(row[1:])
    
result = [-1,-1,INF]

for i in range(1,n+1) :
    for j in range(1,n+1) :
        temp = []
        if i == j : 
            continue
        for k in range(1,n+1) :
            temp.append(min(shortest_paths[i][k]*2, shortest_paths[j][k]*2))
        # print("test : ",i,j,sum(temp),temp)
        
        if sum(temp) < result[2] :
            result = [i,j,sum(temp)]
        
print(" ".join(map(str,result)))