N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()
l = []


def backtracking(depth):
    if depth == M:
        l.append(' '.join(map(lambda x: str(numbers[x]), box)))
        return

    for i in range(N):
        if i in box:
            continue
        # if len(box) != 0 and numbers[i] < box[len(box)-1]:
        #     continue
        box.append(i)
        backtracking(depth + 1)
        box.pop()


box = []
backtracking(0)
check = set()
for i in l:
    if i in check:
        continue
    print(i)
    check.add(i)
