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