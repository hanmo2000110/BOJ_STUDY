import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만드는 방법은 아무 동전도 사용하지 않는 경우 한 가지

for coin in coins:
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])
