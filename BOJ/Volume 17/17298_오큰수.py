'''
오큰수 골드4

접근법 :
왼쪽부터 시작해서 배열을 탐색하며 i번째 숫자보다 큰 수가 나오면 출력한다
만약 i+1, i+2 탐색하다 i번째 숫자보다 크지 않다면 그러한 숫자가 나온 횟수를 저장해둔다.
그리고 i번째 수보다 큰 수가 발견되면 그 수만큼 출력한다.
는 틀렸다

이걸 어떻게 풀지
스택으로 푼다
스택을 사용하면 왼쪽부터 체크하지 않고 오른쪽부터 체크할 수 있어 불필요한 탐색을 방지할 수 있다
'''
from collections import deque

n = int(input())
l = list(map(int, input().split()))

stack = deque()
result = ['-1'] * n
i = 1
stack.append(0)

while True:
    if i >= n:
        break
    while len(stack) != 0:
        t = stack.pop()
        if l[t] < l[i]:
            result[t] = str(l[i])
        else:
            stack.append(t)
            break
    stack.append(i)
    i += 1

print(" ".join(result))
