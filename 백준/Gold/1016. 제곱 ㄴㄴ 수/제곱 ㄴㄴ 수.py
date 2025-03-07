
min,max = map(int,input().split())
check = [True] * (max-min+1)
result = 0

for i in range(2, int(max**0.5) + 1) :
    temp = ((min + i**2 - 1) // i**2) * i**2

    while max >= temp :
        if temp >= min and check[temp-min]:
            check[temp-min] = False
            result += 1
        temp += i**2

print((max-min+1) - result)