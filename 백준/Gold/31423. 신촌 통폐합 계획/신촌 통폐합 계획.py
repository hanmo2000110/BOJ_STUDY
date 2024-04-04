import sys
input=sys.stdin.readline
n=int(input())
name=[0]+list(input().strip() for _ in range(n))
lastindex=[i for i in range(n+1)]
nextindex=[i for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    
    nextindex[lastindex[a]]=b
    lastindex[a]=lastindex[b]
    
for i in range(n):
    print(name[a],end="")
    a=nextindex[a]