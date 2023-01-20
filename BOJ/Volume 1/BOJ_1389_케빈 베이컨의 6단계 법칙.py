n, m = map(int, input().split())
l = [[float('inf')]*(n) for i in range(n)]

# print(l)
for i in range(m):
    a, b = map(int, input().split())
    l[a-1][a-1] = 0
    l[b-1][b-1] = 0
    l[a-1][b-1] = 1
    l[b-1][a-1] = 1

# print(l)

for k in range(n):
    for i in range(n):
        for j in range(n):
            l[i-1][j-1] = min(l[i-1][j-1], l[i-1][k-1] + l[k-1][j-1])
# print(l)
m = float('inf')
m_id = -1
for i in range(n):
    if m > sum(l[i]):
        m = sum(l[i])
        m_id = i+1

print(m_id)

'''
케빈 베이컨의 6단계 법칙 실버1
https://www.acmicpc.net/problem/1389
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 플로이드–워셜

접근법 :
탐색을 해야 하니 bfs를 떠올렸지만 분류에 플로이드 워셜이 있는걸 보고
플로이드 워셜을 공부해서 풀어보려고 한다.
https://chanhuiseok.github.io/posts/algo-50/ 플로이드 워셜 공부 참고

2D 배열을 만들어 각 노드마다 최단 경로를 갱신한다
그리고 모든 경로를 향하는 최단경로의 합이 가장 적은 노드가 답이다.

플로이드 워셜로 푸니까 확실히 간단하다 
플로이드 워셜은 N^3 의 알고리즘이라 유저수가 100이하인 문제여서 사용 가능했다 

'''
