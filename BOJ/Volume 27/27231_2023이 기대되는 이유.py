

'''
2023년이 기대되는 이유 골드5
https://www.acmicpc.net/problem/27231
백트레킹, 브루트포스

접근법 :
최대 1000개의 입력
입력되는 숫자는 최소 1 최대 10**9 => 10자리 지만 실질적으로 10**9 는 가능한 경우의 수가 무수히 많기 때문에 제외하면 9자리수
예외 케이스 :
    1
    1 이후로 0만 있을때 
그렇다면 최고로 작은 수는 2 가 9자리수를 가기위한 제곱수는 몇개? 
최대 30 

먼저 입력되는 숫자가 1234 라면
1324
1 + 234
12 + 34
123 + 4
를 계산하여 리스트에 저장한뒤 
m 을 대입해가며 n보다 커질때까지 카운트한다

그럼 아마 해결될듯?
응 해결 안돼

2023이라면
2 0 2 3 
20 2 3
2 0 23
202 3
2 023
2023 
등과 같은 조합이 등장한다

만약 숫자 길이가 늘어난다면?
123456
1 2 3 4 5 6
12 3 4 5 6 
1 23 4 5 6
1 2 34 5 6
1 2 3 45 6
1 2 3 4 56
123 4 5 6
...
12 34 4 5
12 3 4 56
...
1234 5 6
등과 같은 무수히 많은 경우의 수가 존재한다
이 경우의 수들을 구해 m을 대입했을때 나오는 값과 비교하면 풀 수 있는데
저 무수히 많은 경우의 수를 구하는 코드를 못 짜겠다
포기

숫자들의 조합을 구하는 코드를 찾음
이를 이용해서 해결해보겠음 그 후에 코드 공부 해봐야지
https://www.geeksforgeeks.org/combinations-string-digits/

일단 문제점이 두가지 있었고 그 문제들 떄문에 갖가지 삽질을 했으며 결국 찾아내었다
1. 예외 조건문 :
1이거나 1로시작해 0만 있는 숫자를 걸러내었었는데 문자열이 0과1로만 이루어져 있다면 모두 걸러야했다

2. m이 양의 정수라는 사실을 망각했다 :
하... 담부턴 문제를 잘 읽고 잘 정리해서 시작해야겠다 이거 때문에 몇시간을 버린지 모르겠다

그래도 일단 풀어서 기분은 좋다
숫자 조합 만드는법은 따로 공부해야 할듯
'''


def printCombinations(input, index, output, outLength):
    if (len(input) == index):
        output[outLength] = '\0'
        global l
        l.append(sum(list(map(int, "".join(output[:outLength]).split()))))
        return

    output[outLength] = input[index]

    output[outLength + 1] = ' '
    printCombinations(input, index + 1,
                      output, outLength + 2)

    if (len(input) != (index + 1)):
        printCombinations(input, index + 1,
                          output, outLength + 1)


t = int(input())
ts = [input() for i in range(t)]

for n in ts:
    l = []
    output = [0]*513
    output[0] = '\0'
    printCombinations(n, 0, output, 0)

    # print(sorted(l))
    x = 1
    count = 0
    while True:
        s = 0
        for j in range(len(n)):
            s += int(n[j])**x
        # print("s : ", s)
        x += 1
        if x > 100:
            # print("x : ", x)
            break
        if s in l:
            count += 1
    if count > 5:
        print("Hello, BOJ 2023!")
    else:
        print(count)
