from collections import deque

l = int(input())
s = list(map(int, input().split()))
n = int(input())

answer = deque()
b = deque()

s = sorted(s)

for i in range(len(s)):
    answer.append((s[i], -1))
    if i == 0:
        b.append((0, s[i], s[i]-1))
    if i == len(s)-1:
        # b.append((s[i], 1000000001, 1000000001))
        continue
    else:
        b.append((s[i], s[i+1], s[i+1] - s[i] - 1))

b = deque(sorted(b, key=lambda x: x[2]))
# print(b)
while True:
    if len(b) == 0:
        break
    x, y, r = b.popleft()
    # print(x, y, r)
    if r != 0 and y != 1000000001:
        if r == 1:
            answer.append((x+1, -1))
        else:
            if r < n:
                for i in range(1, r+1):
                    answer.append((x+i, (i)*(y - i-x) - 1))
            else:
                for i in range(x+1, x + n//2 + 2):
                    answer.append((i, (i-x)*(y-i)-1))
                for i in range(y-1, y-1-n//2 - 1, -1):
                    answer.append((i, (i-x)*(y-i)-1))

for i in range(100):
    answer.append((s[-1] + i + 1, float('inf')))

# answer = sort_deque(answer, lambda x: x[1], lambda x: x[])
answer = deque(sorted(answer, key=lambda x: (x[1], x[0])))
# print(answer)

count = 0
t = len(answer)
while len(answer) != 0:
    if count == n:
        break
    x, y = answer.popleft()
    count += 1
    print(str(x), end=" ")
