from sys import stdin as s
import heapq
#제출 시 주석 필수


[house_num, load_num] = list(map(int, input().split(' ')))
input_arr=[];
graph=[[] for _ in range(house_num+1)]
    
for i in range(load_num):
   [start, end, w] = list(map(int, s.readline().split(' ')));
   #양방향 그래프 생성
   graph[start].append([w, end]);
   graph[end].append([w, start]);

INF=1e9;
#방문체크 배열 (INF로 초기화)
visited=[INF] * (house_num+1); 
visited[1] = 0; # 시작점 1은 초기화

q=[];

#시작 (정점 1)
heapq.heappush(q, [0,1])
while(q):
    [w, v] = heapq.heappop(q);
    #visited 배열의 기존값과 비교
    if (visited[v] < w):
        #볼 필요 없음
        continue; 
    for connected_w, connected_v in graph[v]:
        if (connected_w + w < visited[connected_v]):
            # 갱신 필요
            visited[connected_v] = connected_w + w ;
            # 이 점으로 뻗어나가야함
            heapq.heappush(q, [visited[connected_v], connected_v])
            
print(visited[house_num]);