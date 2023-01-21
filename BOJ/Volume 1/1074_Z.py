
'''
Z 실버1

접근법 :
분할 정복으로 풀면 된다.
해보겠다
사등분 해서 왼쪽 위 오른쪽 위 왼쪽 아래 오른쪽 아래 순으로 체크하며
결과값을 누적시킨다.

여러 시도를 해보았다 
재귀를 안 쓰고 풀어보려고 했는데 가능은 해보이는데 재귀가 더 쉬워 보여서 중간에 갈아엎었다
조건문 논리 짤 때 분명 쉬운 조건문인데 잠을 덜 자서인지 집중이 잘 안되고 헷갈려서 삽질을 많이 했다
알고리즘 문제는 정신 말짱할 때 풀어야겠다...
분할 정복이 어떤 느낌인지 알 수 있어서 좋았다

'''
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
