'''
경로 찾기 실1
https://www.acmicpc.net/problem/11403
- 그래프 이론
- 그래프 탐색
- 플로이드–워셜

접근법 :
플로이드 워셜은 보통 최단경로 구할 때 쓴다고 알고 있는데 
이번에 최단경로가 아닌 그저 연결되어 있는가만 체크하면 된다

1. i번째 줄의 i번째 숫자는 항상 0이다.
2. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 
   0인 경우는 없다는 뜻이다.
   
첫 제출에 WC가 나왔다
이유는 max(,max) 형식으로 플로이드 워셜을 사용했는데 이는 잘못된 사용이었다
첫번째 max는 존재하는 경로가 있다면 무조건 1이 뜨고 둘 모두에게 존재하지 않는다면 0이 뜬다
안쪽 min은 플로이드 워셜로 검증중인 k번째 노드가 둘 모두에게 연결되어 있는 검사한다.
만약 둘중에 하나라도 연결이 되어있지 않다면 min으로 인해 0이 리턴된다.
'''

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] = max(a[i][j], min(a[i][k], a[k][j]))

for i in range(n):
    print(" ".join(map(str, a[i])))
