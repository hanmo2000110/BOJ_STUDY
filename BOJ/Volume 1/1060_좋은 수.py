'''
좋은 수 골드1

접근법 :
솔직히 처음 봤을 때 뭔소리 하는지 이해 안됐다
다시 여러번 읽어보았다

간단하게 보면 포함하고 있는 구간의 수가 적을수록 좋은수다
0개인 집합 S에 속하는 수는 이미 좋은 수이고
집합 S에 속하는 수 사이에 있는 수는
    1. 두 수의 차이가 2 이상이라면 두수에 가까울 수록 속하는 범위의 수가 적다
    2. 2 미만이라면 1이니 그 수는 속하는 구간이 없으므로 0이다
    3. 만약 N개 의 숫자를 집합에 속하는 수에 가까운 숫자들로 구성했는데도 자리가 남는다면 집합의 가장 큰수의 다음 숫자들을 출력하면 된다.

나름대로 해결해보겠다고 정렬 여러번 해가면서 시도해봤지만 결국 실패했고
(27퍼까진 잘 돌아가다 27퍼에서 틀렸습니다 뜸 하... 뭐가 문제지)
다른 사람들의 코드를 확인하던 중 heapq 를 사용하면 정렬을 귀찮게 여러번 안 해줘도 되었다는 것을 깨달았다

자체 피드백 :
1. heapq를 사용했다면 정렬을 덜 사용할 수 있었다
2. 정렬 기준이 되는 값의 계산식이 불완전했었다 그래서 27%에서 계속 틀렸었던듯
    2.1 올바른 계산식은 f(x) = (범위의마지막 - x)(x + 범위의 처음) 
    2.2 위의 함수는 위로 볼록한 함수이다 따라서 범위의 한가운데로 갈수록 f(x) 의 값은 커진다.

'''
from collections import deque

l = int(input())
s = list(map(int, input().split()))
n = int(input())

answer = deque()
b = deque()

s = sorted(s)

for i in range(len(s)):
    answer.append((s[i], -1))
    if i == 0:
        b.append((0, s[i], s[i]-1))
    if i == len(s)-1:
        # b.append((s[i], 1000000001, 1000000001))
        continue
    else:
        b.append((s[i], s[i+1], s[i+1] - s[i] - 1))

b = deque(sorted(b, key=lambda x: x[2]))
# print(b)
while True:
    if len(b) == 0:
        break
    x, y, r = b.popleft()
    # print(x, y, r)
    if r != 0 and y != 1000000001:
        if r == 1:
            answer.append((x+1, -1))
        else:
            if r < n:
                for i in range(1, r+1):
                    answer.append((x+i, (i)*(y - i-x) - 1))
            else:
                for i in range(x+1, x + n//2 + 2):
                    answer.append((i, (i-x)*(y-i)-1))
                for i in range(y-1, y-1-n//2 - 1, -1):
                    answer.append((i, (i-x)*(y-i)-1))

for i in range(100):
    answer.append((s[-1] + i + 1, float('inf')))

# answer = sort_deque(answer, lambda x: x[1], lambda x: x[])
answer = deque(sorted(answer, key=lambda x: (x[1], x[0])))
# print(answer)

count = 0
t = len(answer)
while len(answer) != 0:
    if count == n:
        break
    x, y = answer.popleft()
    count += 1
    print(str(x), end=" ")
