n, m = map(int, input().split())
arr = []
count = 0
flag = [0]

dx = [-1,0,1]
dy = [-1,0,1]

def dfs(x,y,flag) :
    if check[x][y] == 1 :
        flag[0] = 1
        return

    check[x][y] = 1
    for i in dx :
        for j in dy :
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m or i == 0 and j == 0:
                continue
            if arr[x][y] < arr[nx][ny] :
                flag[0] = 1
            elif arr[x][y] == arr[nx][ny] and check[nx][ny] == 0:
                dfs(nx,ny,flag)
    

for i in range(n) :
    arr.append(list(map(int,input().split())))

check = [[0 for j in range(m)] for i in range(n)]

for i in range(n) :
    for j in range(m) :
        flag[0] = 0
        dfs(i,j,flag)
        if flag[0] == 0 :
            count += 1

print(count)