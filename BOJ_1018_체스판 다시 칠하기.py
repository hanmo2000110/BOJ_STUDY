n, m = map(int, input().split())
data = [list(input()) for x in range(n)]
# for i in range(n):
#     data.append(list(input()))

min = 64
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        for c in ['W', 'B']:
            count = 0
            expected = c
            for a in range(8):
                for b in range(8):
                    if data[i+a][j+b] != expected:
                        count += 1
                    if b == 7:
                        continue
                    elif expected == 'W':
                        expected = 'B'
                    elif expected == 'B':
                        expected = 'W'

            if count < min:
                min = count

print(min)
