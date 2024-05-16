def solution(n):
    answer = 0
    pibo = [1,1]
    i = 2
    
    if n == 1 :
        return 1
    
    while i != n+1 :
        pibo.append(pibo[i-1] + pibo[i-2])
        i += 1

    
    return (pibo[n])%1234567

