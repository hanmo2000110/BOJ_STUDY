'''
적록색약 골드5

접근법 dfs로 구현할 생각이며 
일반인 용, 적록색약 용 모드를 나눠 하나의 함수로 다 구현할 생각이다.
RecursionError 가 발생했고 이를 해결하기 위해 재귀 함수를 실행하기 전 파라미터로 넘길 다음 인덱스가 올바른 인덱스인지 판별 후 넘겼지만 여전했다
이는 N 이 최대 100이며 모두 하나의 색으로 되어있을 시 첫번째 재귀 함수 호출만으로도 모든 그래프가 탐색되어야 하기 떄문인 것 같다
그래서 해결 방법은 두가지이며 
    1. 재귀를 사용하지 않고 스택을 사용하여 풀던가
    2.sys.setrecursionlimit(10 ** 5) 를 사용하여 재귀함수 깊이 제한을 늘리는 것이다 (기본적으로 1000으로 설정되어 있다)

10^6으로 늘려보았더니 메모리 오류가 발생했고 10^5으로 바꾸니 정답으로 인정되었다.
여러번 시도를 해 3000까지는 통과되었다.

재귀를 이용해 풀었더니
첫 성공엔 255024KB
최대재귀제한을 3000으로 줄이니 130864KB 까지 내려왔다

하지만 스택을 이용해서 푼 사람들은 보면 3만 언저리 인 것을 보아 재귀가 확실히 메모리를 더 많이 잡아먹는 듯하다.

근데 메모리제한 128MB 라고 적혀있는데 왜 내 코드 패스 처리된거지?
파이썬은 메모리 여유 더 주나? 좀 의문이다.
찾아보니 파이썬은 시간제한*2+128mb 란다 신기하구만

'''

import sys


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


sys.setrecursionlimit(10 ** 5)
n = int(input())
g = [[*input()] for n in range(n)]
check = [[False]*n for i in range(n)]

c = 0
c_b = 0

for i in range(n):
    for j in range(n):
        c += dfs(i, j, g[i][j], 0)

check = [[False]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        c_b += dfs(i, j, g[i][j], 1)


print(c, c_b)
