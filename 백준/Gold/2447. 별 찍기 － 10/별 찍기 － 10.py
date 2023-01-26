def makeBlank(xs, xe, ys, ye):
    for i in range(xs, xe):
        for j in range(ys, ye):
            a[i][j] = " "


def recur(xs, ys, size):
    if size == 1:
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                makeBlank((size//3)*i + xs, (size//3)*(i+1) + xs,
                          (size//3)*j + ys, (size//3)*(j+1) + ys)
            else:
                recur((size//3)*i + xs, (size//3)*j + ys, size//3)


n = int(input())
a = [['*'] * n for _ in range(n)]
recur(0, 0, n)

for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print()
