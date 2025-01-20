import sys
sys.setrecursionlimit(1000)  # 재귀 깊이 증가

def check(x,y,arr):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]        
        if arr[nx][ny] == 0 :
            return True
    return False

def robot(x,y,d,arr) :
    global result
    global end

    if arr[x][y] == 0 :
        result += 1
        arr[x][y] = -1
    
    if check(x,y,arr) :
        for k in range(1,5):
            t = (d-k)%4
            nx = x + dx[t]
            ny = y + dy[t]
            if arr[nx][ny] != 0 :
                continue
            robot(nx,ny,t,arr)
    else :
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 1:
            print(result)
            exit()

        robot(nx,ny,d,arr)
    return

N,M = map(int, input().split())
R,C,D = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
end = False

robot(R,C,D,arr)
 # 각 요소를 2자리로 맞춰서 출력