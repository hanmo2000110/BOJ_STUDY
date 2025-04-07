from collections import Counter

# 입력
n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# A와 B의 모든 합을 미리 계산해서 Counter에 저장
AB_sum = Counter()
for a in A:
    for b in B:
        AB_sum[a + b] += 1

# C와 D의 모든 합에 대해 - (c + d) 가 AB_sum에 있는지 확인
count = 0
for c in C:
    for d in D:
        target = -(c + d)
        count += AB_sum.get(target, 0)

print(count)
