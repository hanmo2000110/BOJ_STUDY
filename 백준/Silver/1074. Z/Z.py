import sys


def recursion(s1, s2, e1, e2, n):
    if n == 0:
        return 0
    result = 0
    m1 = (s1+e1)/2
    m2 = (s2+e2)/2

    if r < m1 and c < m2:
        return result + recursion(s1, s2, m1, m2, n-1)
    else:
        result += (2**(n-1))*(2**(n-1))

    if r < m1 and c >= m2:
        return result + recursion(s1, m2, m1, e2, n-1)
    else:
        result += (2**(n-1))*(2**(n-1))

    if r >= m1 and c < m2:
        return result + recursion(m1, s2, e1, m2, n-1)
    else:
        result += (2**(n-1))*(2**(n-1))

    if r >= m1 and c >= m2:
        return result + recursion(m1, m2, e1, e2, n-1)
    else:
        result += (2**(n-1))*(2**(n-1))

n, r, c = map(int, input().split())
sys.setrecursionlimit(10 ** 5)

print(recursion(0, 0, 2**n, 2**n, n))