s = input().strip()
n = len(s)

if s[0] == '0':  # 첫 글자가 0이면 해석 불가
    print(0)
    exit()

dp = [0] * (n + 1)
dp[0] = dp[1] = 1  # 빈 문자열과 첫 번째 문자 해석 경우의 수

for i in range(2, n + 1):
    one_digit = int(s[i - 1])      # 현재 한 자리 숫자
    two_digit = int(s[i - 2:i])    # 앞자리와 합친 두 자리 숫자

    if one_digit > 0:  # 단독 해석 가능
        dp[i] += dp[i - 1]
    
    if 10 <= two_digit <= 26:  # 두 자리 숫자로 해석 가능
        dp[i] += dp[i - 2]

print(dp[n] % 1000000)  # 문제 조건에 따라 1000000으로 나눈 나머지 출력
