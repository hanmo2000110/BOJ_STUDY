import sys
input = sys.stdin.readline

min_val, max_val = map(int, input().split())
check = [True] * (max_val - min_val + 1)

for i in range(2, int(max_val**0.5) + 1):
    square = i * i
    start = ((min_val + square - 1) // square) * square  # min 이상에서 가장 가까운 제곱수 배수 찾기
    
    for j in range(start, max_val + 1, square):
        check[j - min_val] = False  # 해당 수를 제거

print(sum(check))  # 남아있는 True 개수 출력
