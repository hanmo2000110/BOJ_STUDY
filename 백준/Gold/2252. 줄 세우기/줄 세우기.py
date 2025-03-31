from collections import deque

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)] 
degre = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    degre[b] += 1


dq = deque()
while True:

    for i in range(1,n+1):
        if degre[i] == 0:
            dq.append(i)
            print(i, " ")
            degre[i] -= 1
    
    if len(dq) == 0:
        break

    while dq : 
        now = dq.popleft()
        for temp in arr[now]:
            degre[temp] -= 1