
n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n) : 
    for j in range(i + l[i][0], n + 1) :
        if dp[j] < dp[i] + l[i][1] :
            dp[j] = dp[i] + l[i][1]

print(dp[-1])