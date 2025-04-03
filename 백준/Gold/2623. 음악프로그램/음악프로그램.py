from collections import deque

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
dg = [0] * (n+1)
check = [False for _ in range(n+1)]
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
    
for i in range(m):
    for j in range(1,len(l[i])-1) :
        a = l[i][j]
        b = l[i][j+1]
        dg[b] += 1
        arr[a].append(b)
    
dq = deque()
result = []
for i in range(1,n+1):
    if dg[i] == 0:
        dq.append(i)
        
while dq :
    now = dq.popleft()
    check[now] = True
    result.append(now)
    for next in arr[now]:
        dg[next] -= 1
        if dg[next] == 0:
            dq.append(next)
        
if len(result) != n:
    print(0)
else :
    for num in result:
        print(num)