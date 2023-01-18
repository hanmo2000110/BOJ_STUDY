def checkPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input())
nList = list(map(int, input().split()))
sum = 0
for num in nList:
    if checkPrime(num):
        sum += 1

print(sum)

"""
소수 찾기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	149190	69752	55883	46.687%
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3

접근법 :
숫자 입력 받고 그냥 소수 판별하면 된다.
1000이하의 자연수와 숫자 개수는 최대 100이니
100000 충분히 2초안에 해결할 수 있는 문제이다
"""
