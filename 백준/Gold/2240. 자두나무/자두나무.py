T,W = map(int, input().split())
dp = [[0 for _ in range(T+1)] for _ in range(W+1)]
inp = [int(input()) for _ in range(T)]

for i in range(1,T+1):
    if inp[i-1] == 1 :
        dp[0][i] = dp[0][i-1] + 1
    else :
        dp[0][i] = dp[0][i-1]

for i in range(1,W+1):
    for j in range(1,T+1):
        pre = dp[i][j-1]
        new = dp[i-1][j-1]
        if i%2 == 1 : 
            pre += inp[j-1] - 1
            new += inp[j-1] - 1
        else :  
            pre += abs(inp[j-1] - 2)
            new += abs(inp[j-1] - 2)

        dp[i][j] = max(pre,new)

result = 0
for i in range(W+1):
    result = max(result, dp[i][-1])
    
print(result)