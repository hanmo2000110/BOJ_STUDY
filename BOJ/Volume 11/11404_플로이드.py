'''
플로이드 골4
https://www.acmicpc.net/problem/11404
- 그래프 이론 
- 플로이드–워셜

문제 이름부터 플로이드 인것을 보아 플로이드 워셜로 풀면 될 것 같다

다 풀었는데 WC 받아서 알아보니 노선이 하나도 없는 도시도 있을 수 있어
최대값을 그대로 가지고 있는 경우도 있을 수 있어 조건문으로 0으로 출력하도록 해줘야 한다
'''
from sys import stdin

n = int(input())
m = int(input())
a = [[int(1e9)] * (n+1) for _ in range(n+1)]

for _ in range(m):
    fr, to, val = map(int, stdin.readline().split())
    a[fr][to] = min(val, a[fr][to])


for i in range(1, n+1):
    a[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            a[i][j] = min(a[i][j], a[i][k] + a[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j] == int(1e9):
            print('0', end=" ")
            continue
        print(a[i][j], end=" ")
    print()
