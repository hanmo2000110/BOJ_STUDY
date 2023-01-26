a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)
l = [0 for i in range(10)]
for i in n :
    l[int(i)] += 1


print('\n'.join(map(str, l)))
