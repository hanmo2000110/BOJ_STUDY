def solution(s):
    s = list(s.lower())
    
    if s[0].isalpha() :
        s[0] = s[0].upper()
        
    for i in range(len(s)):
        if s[i] == " " and i != len(s)-1:
            if s[i + 1].isalpha() :
                s[i + 1] = s[i + 1].upper()
    
    
    
    return ''.join(s)