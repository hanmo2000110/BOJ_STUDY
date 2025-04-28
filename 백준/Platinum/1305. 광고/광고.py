def get_lps(pattern):
    n = len(pattern)
    lps = [0] * n
    length = 0  # LPS의 길이
    i = 1
    
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def min_ad_length(pattern):
    n = len(pattern)
    lps = get_lps(pattern)
    # 최소 광고 문장 길이 계산: 전체 길이 - 마지막 LPS 값
    return n - lps[-1]

# 입력 받기
n = int(input())  # 광고 문장의 길이
pattern = input()  # 광고 문장

# 결과 출력
print(min_ad_length(pattern))
