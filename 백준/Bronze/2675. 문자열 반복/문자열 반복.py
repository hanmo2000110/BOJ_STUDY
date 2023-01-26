n = int(input())

for i in range(n) :
    num,s = map(str,input().split())
    for c in s :
        print(c * int(num) , end="")
    print()
