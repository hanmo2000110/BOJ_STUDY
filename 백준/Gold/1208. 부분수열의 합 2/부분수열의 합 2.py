from itertools import combinations
from bisect import bisect_left, bisect_right

def get_all_sums(arr):
    result = []
    n = len(arr)
    for i in range(n + 1):  # 부분수열의 길이
        for comb in combinations(arr, i):
            result.append(sum(comb))
    return result

def count_target_sum(A, B, S):
    A.sort()
    B.sort()

    count = 0
    for a in A:
        target = S - a
        left = bisect_left(B, target)
        right = bisect_right(B, target)
        count += (right - left)
    return count

# 입력
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 중간에서 나누기
mid = n // 2
left = arr[:mid]
right = arr[mid:]

# 각각의 부분수열 합 구하기
left_sums = get_all_sums(left)
right_sums = get_all_sums(right)

# 정렬된 리스트에서 이분 탐색으로 개수 찾기
answer = count_target_sum(left_sums, right_sums, s)

# s == 0이면 공집합 (합 0) 제외해야 함
if s == 0:
    answer -= 1

print(answer)
