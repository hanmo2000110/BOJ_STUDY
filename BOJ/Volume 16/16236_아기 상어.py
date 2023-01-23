'''
아기 상어 골3
https://www.acmicpc.net/problem/16236
- 구현
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 시뮬레이션

접근법 :
아기상어는 2로 시작
상하좌우로 움직일 수 있으며 한칸씩 움직이는데 1초
자신보다 큰 물고기가 있는 칸은 못감
자신보다 작은 물고기만 먹을 수 있음
자신과 크기가 같은 물고기는 지나갈 수 있음
자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1증가

이동 로직 :
- 더 이상 먹을 물고기가 없다면 끝
- 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면 거리가 가장 가까운 고기를 먹으러 간다
- 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기 그러한 물고기가 여러마리라면 가장 왼쪽

1. 각 숫자의 갯수를 저장해둔다
잡아먹을 때마다 한개씩 줄인다. 엄마 상어를 불러야 할지 판별할 떄 사용한다
자신보다 작은 물고가가 더 이상 없을 때

2. 물고기들을 잡아먹고 다닐 때 걸리는 총 시간을 저장해두어야 한다.

3. 아기 상어가 현재 위치한 좌표도 저장해야 한다. 

4. bfs 로 체크하는 순서를 위 -> 왼 -> 아래 -> 오른 순으로 한다면 
최단경로를 찾았을 때 같은 최단 경로가 존대하더라도 가장 먼저 찾은 경로가
가장 위 그리고 왼쪽일 것이다.

이거 틀림

4.0. 먹을 수 있는 모든 물고기를 리스트에 담고 조건을 맞춰 정렬 후 0번째 물고기를 먹도록 해야함 

5. 9를 입력받은 후 꼭 0으로 바꿔주어야 한다.

후기 :
구현만 꼼꼼히 하면 된다.
'''
from collections import deque
from functools import cmp_to_key

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def comp(x, y):
    if x[2] < y[2]:
        return -1
    elif x[2] == y[2]:
        if x[0] < y[0]:
            return -1
        elif x[0] == y[0]:
            if x[1] < y[1]:
                return -1
            else:
                return 1
        else:
            return 1
    else:
        return 1


def bfs(baby):
    time_count = 0
    shark_size = 2
    eat_count = 0

    # 반복을 돌리며 엄마 상어를 부를 때까지 반복
    while count_fishes:
        result = deque()
        fishes = []
        check = [[0]*n for _ in range(n)]
        result.append((baby[0], baby[1], 0))
        flag = 0
        while result:
            t = result.popleft()

            if a[t[0]][t[1]] < shark_size and a[t[0]][t[1]] != 0:
                fishes.append(t)
                continue
                # print(t)

            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if x >= n or x < 0 or y >= n or y < 0:
                    continue
                elif check[x][y] == 1:
                    continue
                elif a[x][y] > shark_size:
                    continue
                else:
                    result.append((x, y, t[2] + 1))
                    check[x][y] = 1

        if len(fishes) == 0:
            return time_count

        fishes = sorted(fishes, key=cmp_to_key(comp))
        # print(fishes)
        t = fishes[0]
        # print(t)
        count_fishes[a[t[0]][t[1]]] -= 1

        if count_fishes[a[t[0]][t[1]]] < 1:
            del count_fishes[a[t[0]][t[1]]]

        a[t[0]][t[1]] = 0
        eat_count += 1

        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

        time_count += t[2]
        baby = (t[0], t[1])

    return time_count


n = int(input())

a = [[0]*n for _ in range(n)]
count_fishes = {}

for i in range(n):
    ts = input().split()
    for j in range(len(ts)):
        if int(ts[j]) == 9:
            baby = (i, j)
        elif int(ts[j]) in count_fishes:
            count_fishes[int(ts[j])] += 1
        else:
            count_fishes[int(ts[j])] = 1
        a[i][j] = int(ts[j])
        if int(ts[j]) == 9:
            a[i][j] = 0

if 0 in count_fishes:
    del count_fishes[0]
print(bfs(baby))
