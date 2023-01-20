from sys import stdin
import heapq

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
h = []
m = 0

for i in range(k):
    heapq.heappush(h, (-a[i], i))


l = heapq.nsmallest(k, h, key=lambda x: x[0])
s = 0

for i in range(len(l) - 1):
    s += abs(l[i + 1][1] - l[i][1])
m = s

for i in range(1, n - k + 1):
    h.remove((-a[i-1], i-1))
    heapq.heapify(h)
    heapq.heappush(h, (-a[i + k - 1], i + k - 1))

    l = heapq.nsmallest(k, h, key=lambda x: x[0])
    s = 0
    for j in range(len(l) - 1):
        s += abs(l[j + 1][1] - l[j][1])
    m = min(m, s)

print(m)
'''
청소
https://www.acmicpc.net/problem/27232
자료 구조
트리를 사용한 집합과 맵
슬라이딩 윈도우

접근법 :
구간별로 이동거리를 탐색하고 가장 작은 이동거리를 출력한다
이동거리를 구하느 법은 해당 구간의 우선순위를 기준으로 정렬 후 
이동거리 += a[i+1] - a[i]
식으로 구할 생각이다.
따라서 방의 인덱스와 중요도가 모두 필요하니 tuple 을 사용할 생각이다

시간제한에 관해서 고민해보았는데
1 <= 한번에 청소할 구역 <= 청소할 구역 <= 500000

만약 둘 모두 최대값에 가깝다면 오히려 윈도우가 많이 옮겨다니지 않게 되니 시간제한 문제는 없을듯 하고
만약 구역은 크지만 한번에 청소할 구역의 수가 작다면 아마도 (n - k)k = kn + k^2 이지만 가정은 k가 작을 때 이기 때문에 큰 문제는 없을듯 하다
따라서 윈도우만 옮기며 탐색하면 된다.

하지만 정렬 때문에 시간복잡도 계산이 틀릴수도 있을것 같다
이는 한번 해보고 안되면 그떄 고민해보겠다
 
시간제한 맞았다 ㅋㅋㅋㅋ 사실 조금 예상했다 
그러면 시간복잡도를 낮춰야 하는데 흐음 아마 정렬 부분에서 손을 봐야 할 것 같다.

정렬 과정을 날리고 항상 정렬된 채로 있는 heapq 를 사용할까 생각중이다
그치만 이것도 문제가 있다


시간초과 난 코드
from sys import stdin

n, k = map(int, stdin.readline().split())
a = list(map(int,stdin.readline().split()))
q = []
for i in range(len(a)):
    q.append((a[i], i))

m = float('inf')

for i in range(n-k+1):
    ts = sorted(q[i:i+k].copy(), reverse=True)
    s = 0
    for j in range(k-1):
        s += abs(ts[j+1][1] - ts[j][1])
    m = min(m, s)

print(m)

heapq 를 사용해보았지만 중간에서 지난 요소를 삭제한다는 것은
heapq 의 정체성을 파괴하는 것이기 떄문에 결국 heapify를 해주어야 했고
이는 정렬을 하는것과 다를바가 없었다

from sys import stdin
import heapq

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
h = []
m = 0

for i in range(k):
    heapq.heappush(h, (-a[i], i))


l = heapq.nsmallest(k, h, key=lambda x: x[0])
s = 0

for i in range(len(l) - 1):
    s += abs(l[i + 1][1] - l[i][1])
m = s

for i in range(1, n - k + 1):
    h.remove((-a[i-1], i-1))
    heapq.heapify(h)
    heapq.heappush(h, (-a[i + k - 1], i + k - 1))

    l = heapq.nsmallest(k, h, key=lambda x: x[0])
    s = 0
    for j in range(len(l) - 1):
        s += abs(l[j + 1][1] - l[j][1])
    m = min(m, s)

print(m)

그렇다면 나는 무엇으로 시간복잡도를 줄여야 할까 다시 고민이다

B 구현이 좀 많이 힘들었어요 일단 기본적으로 1. 우선순위를 정렬 기준으로 쓰는 셋을 관리해야 함 2. 각 인접한 구간에서 바뀌는 원소를 제외하고는 순서가 유지됨을 관찰해야 함 3. 바뀌는 원소 2개를 슬라이딩윈도우로 제거하고 추가하면서 이동 거리를 관리해야 함 정도의 풀이가 되는데01.15 18:11:56
chromate00 갤로그로 이동합니다.이 제거, 추가에 이 원소가 끝점에 있는지 (=앞쪽 끝 뒤쪽 끝 각각)에 대한 케웍이 또 요구돼서 많이 힘들었어요
이렇게 풀 때 시복도는 (N-K)logK입니다

구글링 끝에 위와 같은 조언을 얻을 수 있었다
골1에 걸맞게 많이 어려운 문제인듯 하다

Class 로 Set를 구현해야 풀 수 있는 문제란다
흐음 처음 보는 유형이라 감도 안 잡힌다 
고수 코드 좀 들여다 보겠다

'''
