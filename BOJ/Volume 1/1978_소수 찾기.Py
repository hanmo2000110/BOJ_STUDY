"""
소수 찾기 실버5

접근법 :
숫자 입력 받고 그냥 소수 판별하면 된다.
1000이하의 자연수와 숫자 개수는 최대 100이니
100000 충분히 2초안에 해결할 수 있는 문제이다
"""


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
