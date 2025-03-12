ans=""
def solve(n,m,k):
    global ans
    if a[n][m]<k:
        return
    if n==0:
        for i in range(0,m):
            ans=ans+"z"
        return
    elif m==0:
        for i in range(0,n):
            ans=ans+"a"
        return
    else:
        left=a[n-1][m]
        if 1<=k and k<=left:
            solve(n-1,m,k)
            ans="a"+ans
        elif left<k:
            solve(n,m-1,k-left)
            ans="z"+ans
        return

a=[[0 for col in range(101)] for row in range(101)]
for i in range(0,101):
    a[i][0]=1
    a[0][i]=1
for i in range(1,101):
    for j in range(1,101):
        a[i][j]=a[i-1][j]+a[i][j-1]
s=input()
l=s.split()
n=int(l[0])
m=int(l[1])
k=int(l[2])
solve(n,m,k)
if ans=="":
    print("-1")
else:
    print(ans)