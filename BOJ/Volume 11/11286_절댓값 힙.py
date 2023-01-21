'''
절댓값 힙 실버1
https://www.acmicpc.net/problem/11286
- 자료 구조
- 우선순위 큐

접근법 :
우선순위큐(heapq) 를 사용한다
데이터를 넣을 때 튜플로 절대값과 기존값을 같이 넣는다 
정렬 기준은 절대값 우선 절대값이 같다면 기존값으로 비교한다
0이 입력되었을 때 pop 하여 출력하고 만약 우선순위큐가 비어있다면 0을 출력한다

후기 :
- heapq 는 custom comparator 를 지원하지 않아 자체적으로 Node라는 클래스를 만들어 
비교 연산자를 오버라이딩 했다 좋은 연습이었다 익숙해져야 한다

- 입력이 10만개다보니 input()으로 받아 TLE 발생
stdin.readline() 으로 대체하니 시간초과 해결

'''
import heapq
from sys import stdin


class Node(object):
    def __init__(self, val: tuple):
        self.val = val

    def __repr__(self):
        return f'{self.val[1]}'

    def __lt__(self, other):
        return self.val[0] < other.val[0] if self.val[0] != other.val[0] else self.val[1] < other.val[1]


n = int(input())
l = []

for i in range(n):
    t = int(stdin.readline())

    if t == 0:
        if len(l) == 0:
            print(0)
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l, Node((abs(t), t)))
