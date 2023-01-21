'''
이중 우선순위 큐 골드4
https://www.acmicpc.net/problem/7662
- 자료 구조
- 트리를 사용한 집합과 맵
- 우선순위 큐

heapq 를 사용해야 한다
평소에 heapq를 많이 사용해보지 않아 푸쉬 팝 정도만 알고 있었는데 
이번 기회에 검색하다 보니
nlargest(), nsmallest() 와 같은 함수들도 있었다
이를 응용해 삭제하고 난 후 리스트를 heapify 하면 될듯 하다
https://docs.python.org/ko/3/library/heapq.html

근데 시간초과 남

이걸 어케 해결하지

구글링해서 공부했다
먼저 minList maxList 두개를 선언하고 
I 가 입력될 때마다 둘 모두에 추가한다 그리고 딕셔너리에 입력된 값을 키값으로 이미 있는 값이라면 1을 더하고 없는 값이라면 1로 설정한다
D 가 입력되면 리스트에서 팝한다 팝한 값이 딕셔너리에 있는지 확인 후 해당 값이 0보다 크다면 그 값을 1 줄인다. 그리고 값이 없다면 앞의 과정을 반복한다.

위의 과정이 완료되면 딕셔너리에 남아있는 값은 둘 중 하나다 0이던가 0이 아니던가
0이라면 리스트에 없는 값이며 0보다 크다면 리스트에 남아있는 값이다.
이제 딕셔너리에서 가장 큰 값과 가장 작은 값을 출력하면 된다

heapq 를 sorting 의 반복을 줄이기 위해서만 사용하고 실질적으로 숫자들의 관리는 딕셔너리로 했다는 점에서 인상적이었다
새로운 방법을 배웠다.
'''
import heapq
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    maxl, minl = [], []
    check = {}
    for i in range(n):
        command, num = stdin.readline().split()
        if command == 'I':
            num = int(num)
            heapq.heappush(minl, num)
            heapq.heappush(maxl, -num)
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        elif int(num) == -1:
            while True:
                if len(minl) == 0:
                    break
                temp = heapq.heappop(minl)
                if temp in check and check[temp] > 0:
                    check[temp] -= 1
                    break
        elif int(num) == 1:
            while True:
                if len(maxl) == 0:
                    break
                temp = heapq.heappop(maxl)
                if -temp in check and check[-temp] > 0:
                    check[-temp] -= 1
                    break

    temp = check.copy()
    for x in temp:
        if temp[x] == 0:
            del check[x]

    if check:
        print(max(check), min(check))
    else:
        print("EMPTY")
