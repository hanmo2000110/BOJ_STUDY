from collections import defaultdict
r, c=map(int, input().split())
grid=[list(str(input())) for _ in range(r)]
user=[]
mad=[]
for i in range(r):
    for j in range(c):
        if grid[i][j]=='I':
            user=(i, j)
        if grid[i][j]=='R':
            mad.append((i, j))
coms=str(input())
dy, dx=[0, 1, 1, 1, 0, 0, 0, -1, -1, -1], [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
def move_I(num):
    global user
    user=(user[0]+dy[int(coms[num])], user[1]+dx[int(coms[num])])
    if 0<=user[0]<r and 0<=user[1]<c:
        if (user[0], user[1]) in set(mad):
            print("kraj {0}".format(num+1))
            quit()
def move_R(num):
    global mad
    counting=defaultdict(int)
    for i in range(len(mad)):
        y, x=mad[i][0], mad[i][1]
        tmp=1e9
        d=-1
        for j in range(1, 10):
            ny, nx=y+dy[j], x+dx[j]
            if 0<=ny<r and 0<=nx<c:
                dist=abs(ny-user[0])+abs(nx-user[1])
                if dist<tmp:
                    tmp=dist
                    d=j
        mad[i]=(mad[i][0]+dy[d], mad[i][1]+dx[d])
        counting[mad[i]]+=1
        if mad[i]==user:
            print("kraj {0}".format(num+1))
            quit()
    new_mad=[]
    for i in range(len(mad)):
        if counting[mad[i]]>1:
            continue
        else:
            new_mad.append(mad[i])
    mad=new_mad[:]
for i in range(len(coms)):
    move_I(i)
    move_R(i)
answer=[['.' for _ in range(c)] for _ in range(r)]
answer[user[0]][user[1]]='I'
for y, x in mad:
    if y==-1 and x==-1:
        continue
    answer[y][x]='R'
for i in range(r):
    print(''.join(answer[i]))