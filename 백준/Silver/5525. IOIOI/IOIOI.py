# 50점 코드
N = int(input())
M = int(input())
S = input()
P = 'IO'*N + 'I'
answer = 0

for i in range(M - len(P)):
    if S[i] == 'I':
        if S[i:i+len(P)] == P:
            answer += 1
print(answer)
# -------------------------------------------------------------
# 100점 코드
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
