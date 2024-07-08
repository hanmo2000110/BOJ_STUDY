import sys
from itertools import combinations

n , m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n)]
houses = []
chickens = []
result = 10000000000001

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            houses.append((i+1,j+1))
        if graph[i][j] == 2 :
            chickens.append((i+1,j+1))

comb_chicken = list(combinations(chickens, m))
for l in comb_chicken:
    temp_result = 0
    for house in houses :
        min_dist = 100000000000000001
        for chicken in l :
            temp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_dist = min(temp,min_dist)
        temp_result += min_dist 
    result = min(result,temp_result)

print(result)