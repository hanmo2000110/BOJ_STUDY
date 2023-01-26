from collections import deque

t = int(input())

for i in range(t):
    command = input()
    n = int(input())
    num = input()[1: -1].split(',')
    if len(num) == 1 and num[0] == '':
        num = []
    d = deque(num)
    mode = 1
    flag = 0
    for i in range(len(command)):
        if command[i] == 'R':
            mode = mode * -1
        elif command[i] == 'D':
            if len(d) == 0:
                print('error')
                flag = 1
                break
            elif mode == 1:
                d.popleft()
            elif mode == -1:
                d.pop()
    if flag == 1:
        continue
    if mode == 1:
        print("[" + ','.join(list(d)) + ']')
    else:
        print("[" + ','.join(reversed(list(d))) + ']')