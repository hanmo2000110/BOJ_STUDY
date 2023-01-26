n = int(input())
n2 = list(map(str, input().split()))
m = int(input())
dic = {}
n1 = list(map(str,input().split()))
for c in n2 :
    dic[c] = c

for i in n1 :
    if i in dic :
        print(1)
    else :
        print(0)

