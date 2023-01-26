from collections import Counter

n, m, b = map(int, input().split())
l = []
for i in range(n) :
    l = l + list(map(int,input().split()))


t = 99999999999999
h = 0

for i in range(257) :
    ac = 0
    rc = 0
    tb = b
    for j in l :
        if j > i :
            rc += j - i
            tb += j - i
        elif i > j :
            ac += i - j

    if t < ac + rc * 2 or ac > tb:
        continue

    t = ac + rc * 2
    h = i

print(t,h)
