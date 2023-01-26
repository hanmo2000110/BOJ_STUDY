from sys import stdin
n = int(input())
l = []
c = 1
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    l.append((a, b))

l = sorted(l, key=lambda x: (x[1], x[0]))
now = l[0]
for i in range(1, n):
    if now[1] <= l[i][0]:
        now = l[i]
        c += 1
print(c)