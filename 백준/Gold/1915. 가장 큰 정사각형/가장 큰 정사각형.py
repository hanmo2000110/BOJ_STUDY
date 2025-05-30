n,m = map(int, input().split())
a = [list(map(int,input().strip())) for _ in range(n)]
dp = [ [0] for _ in range(n) ]

for i in range(m):
    if i != 0:
        dp[0].append(a[0][i])
for i in range(n):
    dp[i][0] = a[i][0]

for i in range(1,n):
    for j in range(1,m):
        if a[i][j] == 0 :
            dp[i].append(0)
        elif a[i][j] == 1 :
            if dp[i-1][j] == dp[i][j-1] and dp[i-1][j] == dp[i-1][j-1] and dp[i-1][j] > 0 :
                dp[i].append(dp[i-1][j]+1)
            else:
                dp[i].append(min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1)
ans = 0
for d in dp:
    ans = max(ans,max(d))
    # print(d)
print(ans**2)