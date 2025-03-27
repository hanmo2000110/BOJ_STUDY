def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b,i):
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a
    elif a > b :
        parent[a] = b
    else :
        print(i+1)
        exit()

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
turns = [tuple(map(int,input().split())) for _ in range(m)]

for i in range(m):
    turn = turns[i]
    union(turn[0],turn[1],i)

print(0)