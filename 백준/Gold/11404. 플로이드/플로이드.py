from sys import stdin

n = int(input())
m = int(input())
a = [[int(1e9)] * (n+1) for _ in range(n+1)]

for _ in range(m):
    fr, to, val = map(int, stdin.readline().split())
    a[fr][to] = min(val, a[fr][to])


for i in range(1, n+1):
    a[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            a[i][j] = min(a[i][j], a[i][k] + a[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j] == int(1e9):
            print('0', end=" ")
            continue
        print(a[i][j], end=" ")
    print()