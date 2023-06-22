import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
villages = list(map(int, input().split()))
rocks = list(map(int, input().split()))

sums = []

for i in range(k-1):
    sums.append((rocks[i], sum(villages[rocks[i]-1:rocks[i+1]-1])))
sums.append((rocks[k-1], sum(villages[rocks[-1]-1:])))

result = sorted(sums, key=lambda x: (-x[1], x[0]))

result = sorted([x[0] for x in result[:m]])

for i in result:
    print(i)
