import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    # parent[a] = min(parent[a], parent[b])
    # parent[b] = min(parent[a], parent[b])
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


sys.setrecursionlimit(10**5)

v, e = map(int, input().split())

l = []
parent = [x for x in range(v+1)]
result = 0

for i in range(e):
    a, b, c = map(int, input().split())
    l.append((a, b, c))

l = sorted(l, key=lambda x: x[2])

for edge in l:
    a, b, c = edge
    if find_parent(a) == find_parent(b):
        continue
    else:
        result += c
        union_parent(a, b)

print(result)
