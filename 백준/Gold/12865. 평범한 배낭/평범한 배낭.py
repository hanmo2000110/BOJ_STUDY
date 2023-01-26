n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if a[j-1][0] > i:
            dp[j][i] = dp[j-1][i]
        else:
            dp[j][i] = max(dp[j-1][i], dp[j-1][i-a[j-1][0]] + a[j-1][1])

print(dp[n][k])