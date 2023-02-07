import sys
import heapq


# 다익스트라
def solution(start):
    visited = [1e9 for _ in range(n + 1)] # 최단거리 테이블
    heap = []
    heapq.heappush(heap, [0, start])
    visited[start] = 0
    while heap:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, num = heapq.heappop(heap) # 거리, 정점 번호

        # 거리가 해당 정점의 저장된 거리보다 크다면 탐색할 필요없음.
        if dist > visited[num]:
            continue

        # 해당 정점과 인접한 정점의 노드를 확인
        for i, j in graph[num]:
            cost = dist + j

            # 인접한 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < visited[i]:
                visited[i] = cost
                heapq.heappush(heap, [cost, i])

    return visited


n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

# 양방향 그래프 표시
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())

a = solution(1) # 1부터 n까지 다익스트라
b = solution(v1) # v1부터 n까지 다익스트라
c = solution(v2) # v2부터 n까지 다익스트라

# 1-v1-v2-n 경우와 1-v2-v1-n 경우중 최단 거리를 구한다.
answer = min(a[v1] + b[v2] + c[n], a[v2] + c[v1] + b[n])

if answer >= 1e9:
    print(-1)
else:
    print(answer)