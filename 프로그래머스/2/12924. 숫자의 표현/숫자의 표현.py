def solution(n):
    answer = set()
    l = [ i for i in range(1,n+1)]
    
    start = 0
    end = 1

    while start < n :
        s = sum(l[start:end])
        if s == n : 
            answer.add(" ".join(map(str,l[start:end])))
            
        if s <= n :
            if end > n :
                start += 1
            end += 1
        elif s > n :
            start += 1
        
    return len(answer)