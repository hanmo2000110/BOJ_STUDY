from collections import deque


def iNotValid(z, x, y):
    if z >= h or z < 0:
        return True
    if x >= n or x < 0:
        return True
    if y >= m or y < 0:
        return True
    return False


m, n, h = map(int, input().split())
l = deque()
a = [[input().split() for __ in range(n)] for _ in range(h)]
check = [[[False] * m for __ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
time = 0
flag = False

for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == '1':
                l.append((i, j, k, 0))

while l:
    t = l.popleft()
    # print(t)
    check[t[0]][t[1]][t[2]]
    time = max(time, t[3])
    for i in range(6):
        z = t[0] + dh[i]
        x = t[1] + dx[i]
        y = t[2] + dy[i]
        if iNotValid(z, x, y):
            continue
        # print(z, x, y)
        if check[z][x][y] == True:
            continue
        if a[z][x][y] == '0':
            l.append((z, x, y, t[3] + 1))
            a[z][x][y] = '1'


for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == '0':
                flag = True
                break

# print(a)

if flag == True:
    print(-1)
else:
    print(time)