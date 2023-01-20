n = int(input())

a = [1000001] * (n+1)
a2 = [""] * (n+1)

a[1] = 0
for i in range(2, n+1):
    a[i] = a[i-1] + 1
    a2[i] = str(i) + " " + a2[i - 1]
    if i % 2 == 0:
        a[i] = min(a[i], a[i // 2] + 1)
        if a[i] > a[i // 2]:
            a2[i] = str(i) + " " + a2[i // 2]
    if i % 3 == 0:
        a[i] = min(a[i], a[i // 3] + 1)
        if a[i] > a[i // 3]:
            a2[i] = str(i) + " " + a2[i // 3]

print(a[n])
print(a2[n] + "1")

"""
1로 만들기 2 실버1
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	17911	8302	6725	47.480%

문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1 
2
예제 출력 1 
1
2 1
예제 입력 2 
10
예제 출력 2 
3
10 9 3 1

접근법 :
1로 만들기 문제와 유사한 같이 다이나믹 프로그래밍 문제이다.
1로 만들기와 다른점은 거쳐온 숫자들을 출력해야 한다는 점이다
가장 적은 횟수를 시행하는 경우의 수를 발견하는 해당 경우의 수의 경로에 
현재 숫자를 더하는 방식으로 구현하면 경로 또한 동적 프로그래밍으로 구할 수 있다

점화식 : 
a[0] = 0
a[i] = min(a[i-1], a[i/2], a[i/3])

    0 1 2 3 4 5 6 7 8 9 10    
a   0 0 1 1 2 3 2 3 3 2 3  


"""
