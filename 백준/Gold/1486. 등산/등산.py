import sys
input = sys.stdin.readline
 
INF = float('inf')

def floyd(values) :
    global n,m,height,time 
    wasd = [(1,0), (-1,0), (0,1), (0,-1)]
    dist = [[INF for j in range(n*m)] for i in range(n*m)]
    
    for i in range(n) :
        for j in range(m) :
            for k in range(4) :
                if i + wasd[k][0] < 0 or i + wasd[k][0] >= n or j + wasd[k][1] < 0 or j + wasd[k][1] >= m :
                    continue
                if abs(values[i][j] - values[i+wasd[k][0]][j+wasd[k][1]]) > height :
                    dist[i*m + j][(i+wasd[k][0])*m + j+wasd[k][1]] = INF
                elif values[i][j] < values[i+wasd[k][0]][j+wasd[k][1]] :
                    dist[i*m + j][(i+wasd[k][0])*m + j+wasd[k][1]] = pow(values[i+wasd[k][0]][j+wasd[k][1]] - values[i][j],exp=2)
                else :
                    dist[i*m + j][(i+wasd[k][0])*m + j+wasd[k][1]] = 1
    
    for k in range(m*n) :
        for i in range(m*n) :
            for j in range(m*n) :
            
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    
    return dist

n,m,height,time = map(int, input().split())
graph = [input().strip() for _ in range(n)]
values = [[0 for i in range(m) ] for _ in range(n)]
    
for i in range(n):
    for j in range(m) :
        if graph[i][j].isupper() == True :
            values[i][j] = ord(graph[i][j]) - ord('A')
        else :
            values[i][j] = 26 + ord(graph[i][j]) - ord('a')

floyd_data = floyd(values)

result = values[0][0]
for i in range(1,n*m) : 
    if floyd_data[0][i] + floyd_data[i][0] <= time :
        result = max(result, values[int(i/m)][i%m])

print(result)