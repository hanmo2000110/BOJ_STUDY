from sys import stdin
n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))

stack = []
res = [0] * n

for i, tower in enumerate(towers):
    while stack and stack[-1][1] <= tower:
        stack.pop()

    if stack:
        res[i] = stack[-1][0]

    stack.append((i + 1, tower))

print(*res, sep=' ')