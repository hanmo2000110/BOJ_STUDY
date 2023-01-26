'''
별 찍기 - 10
https://www.acmicpc.net/problem/2447
- 분할 정복
- 재귀

새내기 시절에 실패했던 문제이다
다시 도전해본다

어렵진 않았다
시작점과 사이즈를 전달하며 *을 공백으로 바꾸는 작업을 했다
'''


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
