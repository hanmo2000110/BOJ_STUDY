
N = int(input())
K = int(input())

start = 0
end = K

while start <= end :
    mid = (start+end)//2
    cnt = 0
    
    for i in range(1,N+1):
        cnt += min(N, mid//i)
    
    if cnt >= K :
        end = mid - 1
        result = mid
    else :
        start = mid + 1

print(result)