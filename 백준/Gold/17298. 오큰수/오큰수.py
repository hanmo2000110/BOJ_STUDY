from collections import deque

n = int(input())
l = list(map(int, input().split()))

stack = deque()
result = ['-1'] * n
i = 1
stack.append(0)

while True:
    if i >= n:
        break
    while len(stack) != 0:
        t = stack.pop()
        if l[t] < l[i]:
            result[t] = str(l[i])
        else:
            stack.append(t)
            break
    stack.append(i)
    i += 1

print(" ".join(result))