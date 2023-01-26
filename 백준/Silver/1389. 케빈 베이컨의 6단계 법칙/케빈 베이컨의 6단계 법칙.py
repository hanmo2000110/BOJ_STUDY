n, m = map(int, input().split())
l = [[float('inf')]*(n) for i in range(n)]

# print(l)
for i in range(m):
    a, b = map(int, input().split())
    l[a-1][a-1] = 0
    l[b-1][b-1] = 0
    l[a-1][b-1] = 1
    l[b-1][a-1] = 1

# print(l)

for k in range(n):
    for i in range(n):
        for j in range(n):
            l[i-1][j-1] = min(l[i-1][j-1], l[i-1][k-1] + l[k-1][j-1])
# print(l)
m = float('inf')
m_id = -1
for i in range(n):
    if m > sum(l[i]):
        m = sum(l[i])
        m_id = i+1

print(m_id)