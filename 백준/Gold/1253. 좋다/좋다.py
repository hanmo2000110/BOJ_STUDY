n = int(input())
nums = sorted(list(map(int, input().split())))
cnt  = 0

if n < 3 : 
    print(0)
    exit()

for k in range(n):
    target = nums[k]
    
    start = 0
    end = n-1

    while start < end :
        if nums[start] + nums[end] == target and start != k and end != k:
            cnt += 1
            # print(target, nums[start] , nums[end])
            break
        elif nums[start] + nums[end] > target :
            end -= 1
            if end == k :
                end -= 1
        elif nums[start] + nums[end] < target :
            start += 1
            if start == k:
                start += 1

        if start == k:
            start += 1
        if end == k :
            end -= 1

print(cnt)