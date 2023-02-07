import sys


def backTraking(a, s):
    # print(a, s)
    if len(s) >= m * 2:
        l.add(s)
        return
    if a > n:
        return
    if len(s) != 0 and a < int(s[-2]):
        return
    backTraking(a, s + str(a) + " ")
    backTraking(a+1, s + str(a) + " ")
    backTraking(a + 1, s)


n, m = map(int, input().split())
l = set()
sys.setrecursionlimit(10**5)
backTraking(1, "")

for i in sorted(list(l)):
    print(i)
