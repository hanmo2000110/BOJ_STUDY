import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))
dp = [[INF, INF, INF] for i in range(n)]

for i in range(3):
    dp[0][i] = rgb[0][i]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb[i][2]

print(min(dp[n-1]))
