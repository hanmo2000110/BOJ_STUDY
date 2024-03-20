import sys
input = sys.stdin.readline
 
def dfs(n,s) :
    global result
    global temp
    for gr in graph[n] :
        if (n,gr[0]) not in visited :
            visited.append((n,gr[0]))
            visited.append((gr[0],n))
            dfs(gr[0],s+gr[1])
        result = max(result,s)
        if result == s :
            temp = n
    return
   

graph = {}
m = 0
result = 0

while 1:
    try:
        a, b, c = map(int, input().split())
        if a not in graph :
            graph[a] = []
        if b not in graph :
            graph[b] = []
            
        graph[a].append((b,c))
        graph[b].append((a,c))
        
        m = max(m,a)
        m = max(m,b)
        
    except: 
        break
if m == 1 or m == 0 :
    print(0)
    exit() 

# print(graph)
visited = []
temp = 1
dfs(1,0)

result = 0
visited = []
dfs(temp,0)
# print(visited)
print(result)