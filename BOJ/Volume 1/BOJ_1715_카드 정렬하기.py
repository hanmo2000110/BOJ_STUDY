'''
카드 정렬하기 골드4
https://www.acmicpc.net/problem/1715
자료 구조, 그리디 알고리즘, 우선순위 큐

접근법 :
정렬 후 a + b 그리고 결과값을 리스트의 앞부분에 어펜드 후 리스트가 끝날때까지
만약 숫자가 하나만 입력된다면 두 리스트를 합칠 필요가 없으니 0번의 비교가 필요함

항상 가장 작은 두개를 합쳐야 하기 때문에 매번 소팅해줘야 한다
매번 정렬을 반복해야 한다면 heapq 사용하겠다
'''

from collections import deque
from heapq import heappush, heappop

n = int(input())
l = []
for i in range(n):
    heappush(l, int(input()))

if n == 1:
    print(0)
    exit()
count = 0
while True:
    a = heappop(l)
    b = heappop(l)
    s = a + b
    count += s
    if len(l) == 0:
        print(count)
        break
    heappush(l, s)
