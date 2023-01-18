# 50점 코드
N = int(input())
M = int(input())
S = input()
P = 'IO'*N + 'I'
answer = 0

for i in range(M - len(P)):
    if S[i] == 'I':
        if S[i:i+len(P)] == P:
            answer += 1
print(answer)
# -------------------------------------------------------------
# 100점 코드
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)


'''
IOIOI 서브태스크다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	23497	6996	5701	31.077%
문제
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

출력
S에 PN이 몇 군데 포함되어 있는지 출력한다.

제한
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
S는 I와 O로만 이루어져 있다.
서브태스크
번호	배점	제한
1	50	
N ≤ 100, M ≤ 10 000.

2	50	
추가적인 제약 조건이 없다.

예제 입력 1 
1
13
OOIOIOIOIIOII
예제 출력 1 
4
OOIOIOIOIIOII
OOIOIOIOIIOII
OOIOIOIOIIOII
OOIOIOIOIIOII
예제 입력 2 
2
13
OOIOIOIOIIOII
예제 출력 2 
2
OOIOIOIOIIOII
OOIOIOIOIIOII

N의 제약이 있다면 브루트포스 풀 수 있다
하지만 제약이 없어진다면 브루트포스는 시간제약에 걸릴 것이다
DP로 풀어볼까 고민도 해봤는데 결국 디피도 N번의 판별 과정은 어차피 거쳐야 한다
그렇다면 눈을 돌려 M길이의 스트링을 보자 잠을 안 잔 머리로는 못 풀 문제라 공부한다 셈 치고
답지 보고 공부하기로 함

50점 짜리는 지금 당장도 짤 수 있는 브루트포스
100점짜리는 S에 IOI가 몇개 이어지는지 체크한다

(IOI가 몇 번 연속되는지 갯수만 찾아서 체크하게 되면 N * 3 정도의 시간으로 문제를 풀 수 있게 된다.
IOI가 발견되면 index를 2개 이동시키고 아닌 경우에는 index를 1개 이동 시키면서 검사한다.)
라고 블로그 주인님이 말씀하심

확실히 코드를 보니까 납득이 간다.
왜 내가 이 방법을 떠올리지 못했을까
문자열 문제도 많이 풀어봐야겠다
'''
