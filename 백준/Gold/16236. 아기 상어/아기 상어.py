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
