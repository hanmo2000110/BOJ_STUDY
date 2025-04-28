def make_table(pattern):
    m = len(pattern)
    table = [0] * m
    j = 0  # 일치하는 접두사 길이
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def KMP_search(text, pattern):
    n, m = len(text), len(pattern)
    table = make_table(pattern)
    result = []
    
    i = 0  # text의 인덱스
    j = 0  # pattern의 인덱스
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - m + 1)  # 1-based index
                j = table[j - 1]
        else:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1
    
    return result

# 입력 처리
T = input()  # 텍스트
P = input()  # 패턴

# KMP 알고리즘을 통해 찾기
positions = KMP_search(T, P)

# 결과 출력
print(len(positions))  # 패턴이 등장한 횟수 출력
if positions:
    print(*positions)  # 패턴이 등장한 위치 출력
