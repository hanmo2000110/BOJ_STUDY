
from collections import deque


def d(s):
    t = str((int(s)*2) % 10000)
    return "0"*(4-len(t)) + str(t)


def s(s):
    if s == "0000":
        return "9999"
    t = str(int(s) - 1)
    return "0"*(4-len(t)) + str(t)


def l(s):
    return s[1:] + s[0]


def r(s):
    return s[3] + s[:3]


def bfs(fr, to):
    check = [0] * 10000
    q = deque()

    q.append((fr, ""))

    while q:
        now, com = q.popleft()
        if now == to:
            return com
        if check[int(d(now))] != 1:
            q.append((d(now), com + "D"))
            check[int(d(now))] = 1
        if check[int(s(now))] != 1:
            q.append((s(now), com + "S"))
            check[int(s(now))] = 1
        if check[int(l(now))] != 1:
            q.append((l(now), com + "L"))
            check[int(l(now))] = 1
        if check[int(r(now))] != 1:
            q.append((r(now), com + "R"))
            check[int(r(now))] = 1


t = int(input())
testCases = []
for _ in range(t):
    a, b = map(str, input().split())
    testCases.append(("0"*(4 - len(a)) + a, "0"*(4 - len(b)) + b))

for testCase in testCases:
    print(bfs(testCase[0], testCase[1]))
