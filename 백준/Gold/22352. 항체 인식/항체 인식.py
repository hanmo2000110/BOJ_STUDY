import sys


def dfs(i, j, before_val, after_val):
    if before[i][j] != before_val:
        return
    
    before[i][j] = after_val

    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and before[ni][nj] == before_val:
            dfs(ni, nj, before_val, after_val)

N, M = map(int, sys.stdin.readline().split())
before = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
after = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 다른 부분 찾기
found = False
for i in range(N):
    for j in range(M):
        if before[i][j] != after[i][j]:
            dfs(i, j, before[i][j], after[i][j])
            found = True
            break
    if found:
        break

# 결과 확인
result = "YES" if before == after else "NO"
print(result)