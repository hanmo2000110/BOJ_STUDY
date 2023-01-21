'''
AC 골드5

접근법 :
요상한 ac언어에는 두가지 기능이 있다
1. R 숫자를 리버스 하는 것이다.
2. D 숫자를 하나 삭제하는 것이다. 만약 삭제할 숫자가 없다면 error를 리턴한다.

처음에 리스트를 R이 들어올 때마다 뒤집어야 할까 고민했지만 너무 비효율적이라고 생각했다
디큐를 사용한다면 앞이나 뒤에서 pop 할 수 있기 때문에 R이 입력될때마다 모드를 바꿔가며 pop 하고
마지막에 출력할 때에도 모드를 따라 뒤집혀있다면 리스트를 reversed()로 뒤집어 출력하도록 했다.
'''

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
                # print(d)
                d.popleft()
            elif mode == -1:
                d.pop()
    if flag == 1:
        continue
    if mode == 1:
        print("[" + ','.join(list(d)) + ']')
    else:
        print("[" + ','.join(reversed(list(d))) + ']')
