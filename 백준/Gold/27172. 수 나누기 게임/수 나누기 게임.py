import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

check = [0] * 1000001
score = [0] * 1000001

for num in numbers:
    check[num] = 1


for i in range(n):
    temp = numbers[i] * 2
    while temp < 1000001:
        if check[temp] == 1:
            score[numbers[i]] += 1
            score[temp] -= 1
        temp += numbers[i]

for i in numbers:
    print(score[i], end=" ")
