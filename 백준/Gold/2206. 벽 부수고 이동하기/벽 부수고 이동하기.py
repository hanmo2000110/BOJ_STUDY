from collections import deque


def bfs():
    result = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    check = [[[False] * 2 for i in range(m)] for _ in range(n)]

    q.append((0, 0, 0, 0))

    while q:
        t = q.popleft()

        if t[0] == n-1 and t[1] == m-1:
            return t[3]

        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]

            if x >= n or x < 0 or y >= m or y < 0:
                continue

            if graph[x][y] == 1 and t[2] == 0:
                if check[x][y][t[2]] == True:
                    continue
                # if t[2] == 0:
                check[x][y][t[2]] = True
                q.append((x, y, 1, t[3] + 1))
            elif graph[x][y] == 1 and t[2] != 0:
                continue
            else:
                if check[x][y][t[2]] == True:
                    continue
                # if t[2] == 0:
                check[x][y][t[2]] = True
                q.append((x, y, t[2], t[3] + 1))
    return -2


n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

print(bfs() + 1)
