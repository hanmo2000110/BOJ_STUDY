from collections import deque

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = [[] for _ in range(n+1)] 
    ancestor = [[] for _ in range(n+1)] 
    degre = [0] * (n+1)
    value = list(map(int, input().split()))
    for _ in range(k):
        a,b = map(int, input().split())
        arr[a].append(b)
        ancestor[b].append(a)
        degre[b] += 1
    w = int(input())
    sortedList = []
    dp = [0] * (n+1)

    dq = deque()
    
    while True:
        for i in range(1,n+1):
            if degre[i] == 0:
                dq.append(i)
                sortedList.append(i)
                degre[i] -= 1

        if len(dq) == 0:
            break
        
        while dq : 
            now = dq.popleft()
            for temp in arr[now]:
                degre[temp] -= 1
    # print(sortedList)

    for num in sortedList:
        temp = 0
        for anc in ancestor[num]:
            temp = max(temp,dp[anc])
        dp[num] = max(dp[num], value[num-1] + temp)
    print(dp[w])