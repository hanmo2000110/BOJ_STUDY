t = int(input())
ts = [input() for i in range(t)]

for n in ts:

    if n == '1':
        print("Hello, BOJ 2023!")
        continue

    if n[0] == '1':
        flag = 0
        for j in range(1, len(n)):
            if n[j] != '0':
                flag = 1
        if flag == 0:
            print("Hello, BOJ 2023!")
            continue
    l = []
    for j in range(len(n)):
        s = 0
        if n[0:j+1] != '':
            s += int(n[0:j+1])
        if n[j+1:] != '':
            s += int(n[j+1:])
        l.append(s)

    print(sorted(l))
    x = 0
    count = 0
    while True:
        s = 0
        for j in range(len(n)):
            s += int(n[j])**x
        print("s : ", s)
        x += 1
        if x > 100:
            print("x : ", x)
            break
        if s in l:
            count += 1
    print(count)

'''
2023년이 기대되는 이유
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

'''
