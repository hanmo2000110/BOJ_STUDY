n = int(input())

man_height = sorted(list(map(float, input().split())))
woman_height = sorted(list(map(float, input().split())), reverse=True)

count = 0

man = 0
woman = 0

# print(man_height)
# print(woman_height)

while man < n and woman < n:
    if man_height[man] * woman_height[woman] > 0:
        if man_height[man] < 0:
            man += 1
        else:
            woman += 1
    elif man_height[man] + woman_height[woman] < 0:
        count += 1
        man += 1
        woman += 1
    else:
        woman += 1

print(count)
