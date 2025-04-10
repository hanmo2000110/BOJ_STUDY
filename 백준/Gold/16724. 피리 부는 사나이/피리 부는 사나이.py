import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
parent = [i for i in range(n * m)]

# 방향 벡터
dir_map = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

for i in range(n):
    for j in range(m):
        cur_idx = i * m + j
        dx, dy = dir_map[board[i][j]]
        ni, nj = i + dx, j + dy
        next_idx = ni * m + nj
        union(cur_idx, next_idx)

# 루트 노드 개수 세기
res = set()
for i in range(n * m):
    res.add(find(i))

print(len(res))
