n = int(input())
villages = [0] * (n)
total = 0
for i in range(n):
    x, a = map(int, input().split())
    villages[i] = (x, a)
    total += a

villages = sorted(villages, key=lambda x: x[0])

s = 0

for i in range(n):
    s += villages[i][1]
    if s >= total/2:
        print(villages[i][0])
        break
