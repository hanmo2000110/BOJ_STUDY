import copy

def pre_dfs() :
    global loca
    for i in range(n):
        for j in range(m):
            if loca[i][j] == '2' :
                dfs(i,j)
                
    return count_map()


def dfs(x,y) :
    global loca
    if x >= n or y >= m or x < 0 or y < 0 :
        return
    if loca[x][y] == '1' : 
        return
    if check[x][y] == 1 :
        return
    loca[x][y] = '2'
    check[x][y] = 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)


def count_map() : 
    global loca
    count = 0
    for row in loca :
        count += row.count('0')
    return count


n,m = map(int, input().split())

location = [input().split() for _ in range(n)]
loca = []
empty = []

for i in range(n) :
    for j in range(m) :
        if location[i][j] == '0' :
            empty.append((i,j))

result = 0

for x1,y1 in empty :
    for x2,y2 in empty :
        if x1 == x2 and y1 == y2 :
            continue
        for x3,y3 in empty :
            if (x3 == x2 and y3 == y2) or (x3 == x1 and y3 == y1) :
                continue
            loca = copy.deepcopy(location)
            check = [[0 for _ in range(m)] for _ in range(n)]
            loca[x1][y1] = '1'
            loca[x2][y2] = '1'
            loca[x3][y3] = '1'
            result = max(result,pre_dfs())
            



print(result)
