n = int(input())

for i in range(n):
    s = input()

    lstart = 0
    lend = len(s) - 1
    rstart = 0
    rend = len(s) - 1
    flag1 = 0
    flag2 = 0
    check = False

    if s == s[::-1]:
        print(0)
        continue

    while True:
        if lstart >= lend:
            check = True
            break

        elif s[lstart] == s[lend]:
            lstart += 1
            lend -= 1
            continue
        else:
            if flag1 == 1 or s[lstart + 1] != s[lend]:
                break
            else:
                lstart += 1
                flag1 = 1

    while True:
        if rstart >= rend:
            check = True
            break
        elif s[rstart] == s[rend]:
            rstart += 1
            rend -= 1
            continue
        else:
            if flag2 == 1 or s[rstart] != s[rend - 1]:
                break
            else:
                rend -= 1
                flag2 = 1

    if check == True:
        print(1)
    else:
        print(2)
