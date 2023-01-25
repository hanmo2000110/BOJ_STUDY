'''
평범한 배낭 골5
https://www.acmicpc.net/problem/12865
- 다이나믹 프로그래밍
- 배낭 문제

DP 문제이니 점화식을 세워보겠다
일단 dp테이블은 무게를 기준으로 하고

점화식 :
DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - W[i]] + V[i]);
'''

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
# print(dp)
