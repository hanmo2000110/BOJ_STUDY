

'''
뱀과 사다리 게임 골드5

접근법 :
이 문제는 그래프 탐색 문제이며 
최단 경로를 구하는 문제는 BFS 로 풀면 된다

주사위를 굴려 나올 수 있는 경우의 수는 1~6
사다리를 만나면 올라가고 뱀을 만나면 내려간다
뱀이나 사다리 정보를 맵으로 받아 키 값으로 접근하도록 하면 사용하기에 편할듯 하다
한번 방문한 노드는 이미 그 노드의 모든 가능성을 디큐에 넣은 상황이기 떄문에 굳이 더 탐색할 필요가 없다
그러니 넘긴다
'''
from collections import deque


def bfs(start, to):
    queue = deque()
    check = [False] * 101
    d = 0
    queue.append((start, 0))

    while queue:
        v, d = queue.popleft()
        # print(v, d)
        if v > 100:
            continue
        if v == to:
            return d
        check[v] = True
        for i in range(6, 0, -1):
            if v+i <= 100 and check[v+i]:
                continue
            if str(v+i) in hm:
                queue.append((hm[str(v+i)], d+1))
            else:
                queue.append((v+i, d+1))


n, m = map(int, input().split())
hm = {}
for i in range(n+m):
    key, value = map(int, input().split())
    hm[str(key)] = value


print(bfs(1, 100))
