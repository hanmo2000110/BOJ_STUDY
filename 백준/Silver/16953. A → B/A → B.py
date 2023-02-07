n, m = input().split()
count = 1
flag = 0

while int(m) >= int(n):
    # print(m)
    if m == n:
        print(count)
        flag = 1
        break
    elif m[-1] == '1':
        count += 1
        m = m[:-1]
    elif int(m) % 2 == 0:
        m = str(int(m)//2)
        count += 1
    else:
        break
if flag == 0:
    print(-1)
