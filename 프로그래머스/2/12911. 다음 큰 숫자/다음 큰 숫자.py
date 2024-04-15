def solution(n):
    target = str(format(n,'b')).count("1")
    while True :
        n = n + 1
        if str(format(n,'b')).count("1") == target :
            return n
        
    return n