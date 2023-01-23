'''
회의실 배정 실1
https://www.acmicpc.net/problem/1931
- 그리디 알고리즘
- 정렬

접근법 :
끝나는 시간 기준으로 정렬 후 현재 시각보다 시작시간이 같거나 늦는 회의를 
선택하는 방법으로 탐색하면 될 듯 싶다 

끝나는 시간을 키1 시작 시간을 키2로 해야 맞다

'''
from sys import stdin
n = int(input())
l = []
c = 1
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    l.append((a, b))

l = sorted(l, key=lambda x: (x[1], x[0]))
now = l[0]
for i in range(1, n):
    if now[1] <= l[i][0]:
        now = l[i]
        c += 1
print(c)
