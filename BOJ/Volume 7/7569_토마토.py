'''
토마토 골5
https://www.acmicpc.net/problem/7569
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

접근법 :
bfs로 구현한다
익은 토마토로 입력받은 좌표들을 모두 queue 에 넣고 반복을 시작하면 될 것 같다.

1. 방문한 토마토는 익음 처리 한다
2. 방문한 토마토는 방문 처리 한다
3. 방문할 토마토가 방문 처리 되어있는지 확인한다
4. 방문할 토마토의 좌표가 올바른지 확인한다.
5. 방문할 때마다 시간에 기존 시간과 현재 노드에 도달하기까지의 시간을 비교 후 큰 값을 저장
    5.1 이는 너비우선탐색이라 그럼 해당 토마토에 가장 먼저 도달한 경로가 최단경로
5. 너비우선탐색이 종료된 후 상자에 익지 않은 토마토가 남아있는지 확인한다.
    5.1. 남아있다면 -1
    5.2. 남아있지 않다면 저장해둔 시간을 출력
    
bfs 문제가 익숙해진것 같다. 골드5 bfs는 풀만 하다
'''
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
    # print(a)
