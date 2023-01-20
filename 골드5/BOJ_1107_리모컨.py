target = input()
n = int(input())
if n == 0:
    print(min(len(str(target)), abs(100-int(target))))
    exit()
bList = list(map(int, input().split()))

if len(bList) == 10:
    print(abs(100-int(target)))
    exit(0)

if target == '100':
    print(0)
    exit(0)

m = abs(100-int(target))
for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(i[j]) in bList:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(i) - 1:
            m = min(m, len(i) + abs(int(target)-int(i)))

print(m)

'''
리모컨 골드5
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	81753	19702	13694	22.616%
문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

예제 입력 1 
5457
3
6 7 8
예제 출력 1 
6
예제 입력 2 
100
5
0 1 2 3 4
예제 출력 2 
0
예제 입력 3 
500000
8
0 2 3 4 6 7 8 9
예제 출력 3 
11117
예제 입력 4 
100
3
1 0 5
예제 출력 4 
0
예제 입력 5 
14124
0
예제 출력 5 
5
예제 입력 6 
1
9
1 2 3 4 5 6 7 8 9
예제 출력 6 
2
예제 입력 7 
80000
2
8 9
예제 출력 7 
2228

접근법 :
먼저 고장난 버튼들은 제외하고 사용 가능한 버튼들로 리스트를 만든다
채널은 500000이하로 나오며 500000은 6자리이다.
하나도 금지되지 않는다면 목표채널의 길이를 출력하고 끝낸다
만약 목표 채널에 바로 갈 수 없다면 아래의 작업을 실행한다

0. 고장난 숫자가 없다면 바로 목표 숫자를 누르는 것과 100에서 목표 숫자로 이동하는 것중 어느것이 더 작은지 비교 후 출력
1. 0부터 1000000까지의 숫자중 목표 숫자에 가까운 숫자를 찾는다
2. 해당 숫자의 길이와 목표와 해당 숫자의 거리를 더하고 이를 100에서 목표채널로 이동하는 거리와 비교 후 출력

계속 이해가 되지 않는 이유로 틀렸습니다 로 나와서 몇시간을 의욕을 잃고 쉬었는데 알고보니 반복문이 시작하기 전에 이상한 코드를 넣어두었었다.
고장난 버튼이 없으면 바로 입력받은 숫자의 길이를 출력하도록 되어있던 것이다. 하지만 예를들어 99 또는 101이 입력되었다고 가정한다면 
101은 자리수이지만 100에서는 + 한번이면 도달할 수 있는 숫자이다. 따라서 내 코드가 틀렸었었다.
'''
