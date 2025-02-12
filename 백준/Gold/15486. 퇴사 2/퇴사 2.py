import sys

# 입력 받기
input = sys.stdin.read
data = input().split("\n")
N = int(data[0])
T, P = [], []

for i in range(1, N+1):
    if data[i]:
        t, p = map(int, data[i].split())
        T.append(t)
        P.append(p)

# DP 배열 초기화
dp = [0] * (N + 2)  # N+1일까지 고려해야 하므로 N+2 크기로 설정

# DP 갱신
for i in range(1, N + 1):
    # 이전까지의 최대 이익 유지
    dp[i] = max(dp[i], dp[i-1])

    # 상담을 할 수 있는 경우, 미래 값 갱신
    end = i + T[i-1]
    if end <= N + 1:
        dp[end] = max(dp[end], dp[i] + P[i-1])

# 결과 출력
print(max(dp))
