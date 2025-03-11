import sys
from collections import deque
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num **0.5)+1):
        if num % i == 0:
            return False
    return True

def bfs(A,B):
    q = deque()
    q.append((A,0))
    while q:
        password, count = q.popleft()
        if password == B:
            return count
        for i in range(4):
            # 각 자리에 0 ~ 9를 넣어가며 소수인지 확인
            for j in range(10):
                new_pass = list(str(password))
                new_pass[i] = str(j)
                new_pass = int(''.join(new_pass))      
                # 1000 이상, 방문 x, 소수 o        
                if 1000 <= new_pass and not visited[new_pass] and isPrime(new_pass):
                    visited[new_pass] = 1
                    q.append((new_pass, count+1))
    
T = int(input())
#소수 판별
prime = [False]
for i in range(1,10000):
    prime.append(isPrime(i))

#테스트 케이스
for _ in range(T):
    A, B = map(int,input().split())
    visited = [0] * 10000
    visited[A] = 1
    result = bfs(A,B)
    print(result if result != None else "Impossible")