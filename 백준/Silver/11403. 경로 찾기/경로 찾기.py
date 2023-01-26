n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] = max(a[i][j], min(a[i][k], a[k][j]))

for i in range(n):
    print(" ".join(map(str, a[i])))