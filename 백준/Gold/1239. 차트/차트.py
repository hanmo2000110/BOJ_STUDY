import sys
from itertools import permutations

def count_center_lines(sequence):
    # 누적합 배열 생성
    prefix_sum = []
    current_sum = 0
    for num in sequence:
        current_sum += num
        prefix_sum.append(current_sum)
    
    # 중심선 개수 세기
    count = 0
    for i in range(len(prefix_sum)-1):
        for j in range(i+1, len(prefix_sum)):
            if prefix_sum[i] + 50 == prefix_sum[j]:
                count += 1
    return count

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# 50보다 큰 수가 있으면 중심선을 만들 수 없음
if max(numbers) > 50:
    print(0)
else:
    # 모든 순열에 대해 최대 중심선 개수 찾기
    max_lines = 0
    for perm in permutations(numbers):
        max_lines = max(max_lines, count_center_lines(perm))
    print(max_lines)