n = int(input())
nums = list(map(int, input().split()))
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

dp = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(i+1):
        dp[i][j] = 1 

for i in range(n-2,-1,-1):
    for j in range(n-1,-1,-1):
        if dp[i+1][j-1] == 1 and nums[j] == nums[i]:
            # print(i,j,dp[i][j])
            dp[i][j] = 1 

for query in queries:
    print(dp[query[0]-1][query[1]-1])