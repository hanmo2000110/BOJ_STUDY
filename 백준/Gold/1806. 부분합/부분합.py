import sys
input = sys.stdin.readline


n, s = map(int, input().split())

l = list(map(int, input().split()))

start = 0
end = 0
partial_sum = 0
length = n+1

while True:
    if partial_sum >= s:
        if end - start < length:
            length = end - start
        partial_sum -= l[start]
        start += 1
    elif end == n:
        break
    elif partial_sum < s:
        partial_sum += l[end]
        end += 1


if length != n+1:
    print(length)
else:
    print(0)
