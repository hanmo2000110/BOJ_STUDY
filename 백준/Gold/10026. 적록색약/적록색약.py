def checkAvailable(x, y, a, b, mode):
    if a >= n or a < 0 or b >= n or b < 0:
        return False
    if check[a][b] == True:
        return False
    if mode == 0:
        if g[x][y] != g[a][b]:
            return False
    else:
        if (g[a][b] == 'G' or g[a][b] == 'R') and g[x][y] == 'B':
            return False
        if g[a][b] == 'B' and g[x][y] != g[a][b]:
            return False
    return True


def dfs(x, y, pre, mode):
    if x >= n or x < 0 or y >= n or y < 0:
        return 0
    if check[x][y] == True:
        return 0

    check[x][y] = True

    if checkAvailable(x, y, x, y-1, mode):
        dfs(x, y-1, g[x][y], mode)
    if checkAvailable(x, y, x, y+1, mode):
        dfs(x, y+1, g[x][y], mode)
    if checkAvailable(x, y, x+1, y, mode):
        dfs(x+1, y, g[x][y], mode)
    if checkAvailable(x, y, x-1, y, mode):
        dfs(x-1, y, g[x][y], mode)
    return 1

import sys
sys.setrecursionlimit(3000)
n = int(input())
g = [[*input()] for n in range(n)]
check = [[False]*n for i in range(n)]

c = 0
c_b = 0

for i in range(n):
    for j in range(n):
        # print("     " + str(i), str(j) + "       ")
        c += dfs(i, j, g[i][j], 0)

check = [[False]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        # print("     " + str(i), str(j) + "       ")
        c_b += dfs(i, j, g[i][j], 1)


print(c, c_b)