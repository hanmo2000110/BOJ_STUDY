import heapq
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    maxl, minl = [], []
    check = {}
    for i in range(n):
        command, num = stdin.readline().split()
        if command == 'I':
            num = int(num)
            heapq.heappush(minl, num)
            heapq.heappush(maxl, -num)
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        elif int(num) == -1:
            while True:
                if len(minl) == 0:
                    break
                temp = heapq.heappop(minl)
                if temp in check and check[temp] > 0:
                    check[temp] -= 1
                    break
        elif int(num) == 1:
            while True:
                if len(maxl) == 0:
                    break
                temp = heapq.heappop(maxl)
                if -temp in check and check[-temp] > 0:
                    check[-temp] -= 1
                    break

    temp = check.copy()
    for x in temp:
        if temp[x] == 0:
            del check[x]

    if check:
        print(max(check), min(check))
    else:
        print("EMPTY")