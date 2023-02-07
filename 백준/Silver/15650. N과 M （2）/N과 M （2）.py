import sys


def backTraking(a, s):
    if len(s) >= m * 2:
        print(s)
        return
    if a > n:
        return
    if len(s) != 0 and a <= int(s[-2]):
        return
    backTraking(a + 1, s + str(a) + " ")
    backTraking(a + 1, s)


n, m = map(int, input().split())
sys.setrecursionlimit(10**5)
backTraking(1, "")
