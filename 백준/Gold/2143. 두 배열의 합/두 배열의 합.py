import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 누적합으로 모든 부분합 구하기
def get_all_sub_sums(arr):
    n = len(arr)
    sub_sums = []
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            sub_sums.append(total)
    return sub_sums

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# A, B의 모든 부분합 구하기
subA = get_all_sub_sums(A)
subB = get_all_sub_sums(B)
subB.sort()

# subA는 기준값, subB는 이분탐색용
count = 0
for a in subA:
    target = T - a
    left = bisect_left(subB, target)
    right = bisect_right(subB, target)
    count += right - left

print(count)
