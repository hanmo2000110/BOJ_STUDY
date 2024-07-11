import sys
from itertools import combinations

N = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] 
allstat = sum(sum_stat) // 2 
result = float('inf')
for l in combinations(sum_stat, N//2):
    result = min(result, abs(allstat - sum(l))) 
print(result)