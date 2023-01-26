t = int(input())
l = [int(input()) for i in range(t)]

a0 = [0] * 41
a1 = [0] * 41
a0[0] = 1
a0[1] = 0
a1[0] = 0
a1[1] = 1
for i in range(2, 41):
    a0[i] = a0[i-1] + a0[i-2]
    a1[i] = a1[i-1] + a1[i-2]

for x in l:
    print(a0[x], a1[x])