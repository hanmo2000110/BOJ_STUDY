'''
DSLR 골4
https://www.acmicpc.net/problem/9019
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

접근법 :
1. 입력되는 모든 숫자들은 0~9999 이다
2. D,S,L,E 명령어들을 함수화 하면 편할것 같다.
3. 불필요한 탐색을 피하기 위해 딕셔너리를 선언하고 체크하면 될 것 같다
4. 시간제한이 6초로 널널하기 때문에 그냥 탐색만 잘하면 되는거 같다. 

시간초과 발생
딕셔너리 -> List 로 바꾸니 7% -> 100% 향상 
숫자 범위가 크지 않다면 리스트로 선언하는게 이득?

매번 str 로 변환하는 과정에서 시간을 많이 잡아먹은듯 하다
다른 빠른 결과들이랑 비교하면 거의 6배 정도 시간 차이가 난다.
코드는 좀 덜 직관적이더라도 내가 고생하는게 나은듯 하다
'''

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
