

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

# 입력 처리
while True:
    T = input().strip()
    if T == ".":
        break
    table = make_table(T)
    
    # 패턴 반복 여부 확인
    repeatLength = len(T) - table[-1]
    
    # 패턴이 반복될 수 있는지 확인
    if len(T) % repeatLength == 0:
        print(len(T) // repeatLength)
    else:
        print(1)
