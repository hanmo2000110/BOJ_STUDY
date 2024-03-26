import sys
input = sys.stdin.readline
 
INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    # 최단 경로 행렬 초기화
    # 0 if i == j else
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    route = [["-" if i == j else j if graph[i][j] != INF else -1 for j in range(n)] for i in range(n)]
    
    # 동적 프로그래밍을 통한 갱신
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    if route[i][k] == -1 :
                        route[i][j] = k
                    else : 
                        route[i][j] = route[i][k]

    return dist, route


v,e = map(int, input().split())
graph = [[INF for _ in range(v+1)] for _ in range(v+1)]

for i in range(e) :
    a,b,c = map(int, input().split())
    
    graph[a][a] = 0
    graph[b][b] = 0
    graph[a][b] = c
    graph[b][a] = c

# print(graph)

shortest_paths,route = floyd_warshall(graph)

# print(route)

for i in range(1,v+1) :
    for j in range(1,v+1) :
        print(route[i][j], end=" ")
    print()


    

    

