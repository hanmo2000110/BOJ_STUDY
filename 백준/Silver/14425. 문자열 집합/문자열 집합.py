N, M = map(int, input().split())

s = set([input() for _ in range(N)])

count = 0
for _ in range(M):
    c = input()
    if c in s:
        count += 1

print(count)