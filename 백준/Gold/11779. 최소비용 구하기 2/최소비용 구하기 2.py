import heapq

def dijkstra(graph, start):
    # 최단 거리 배열을 무한대로 초기화
    dist = [ (float('inf'), "" ) for i in range(N+1)] 
    dist[start] = (0, str(start))  # 시작 노드의 거리는 0

    # 우선순위 큐 (거리, 노드) 형식으로 큐에 삽입
    pq = [(0, start, str(start))]  # (거리, 노드)

    while pq:
        current_dist, current_node, route = heapq.heappop(pq)

        # 이미 방문한 노드라면 skip
        if current_dist > dist[current_node][0]:
            continue

        # 인접한 노드들을 탐색
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # 더 작은 경로가 발견되면 갱신
            if distance < dist[neighbor][0]:
                newRoute =  route + " " + str(neighbor)
                dist[neighbor] = (distance, newRoute)
                heapq.heappush(pq, (distance, neighbor, newRoute))

    return dist

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    fr,to,cost = map(int,input().split())
    graph[fr].append((to,cost))

start,end = map(int,input().split())

ans = dijkstra(graph,start)

print(ans[end][0])
print(len(ans[end][1].split()))
print(" ".join(ans[end][1].split()))