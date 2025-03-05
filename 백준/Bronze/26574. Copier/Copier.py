# 숫자의 개수를 입력
n = int(input())

# n번 반복하여 숫자와 숫자의 복사본을 출력
for _ in range(n):
    # 숫자를 입력
    num = input()
    # 숫자와 숫자의 복사본을 출력
    print(num, num)
