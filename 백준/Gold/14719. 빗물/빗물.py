H, W = map(int, input().split())
limit = list(map(int, input().split()))

result = 0

# 각 위치에서 좌우의 최대 높이를 구하여 빗물이 고이는 양을 계산
left_max = [0] * W
right_max = [0] * W

left_max[0] = limit[0]
for i in range(1, W):
    left_max[i] = max(left_max[i - 1], limit[i])

right_max[W - 1] = limit[W - 1]
for i in range(W - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], limit[i])

for i in range(W):
    result += max(0, min(left_max[i], right_max[i]) - limit[i])

print(result)