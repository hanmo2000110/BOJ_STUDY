H,W = map(int, input().split())
limit = list(map(int, input().split())) 
arr = [[] for _ in range(H)]
result = 0

for i in range(H):
  for j in range(W):
    if i < limit[j] :
      arr[i].append(1)
    else :
      arr[i].append(0)

for i in range(H):
  flag = 0
  for j in range(1,W):
    if arr[i][j] == 0 and arr[i][j-1] == 1 :
      flag = j
    elif arr[i][j] == 1 and flag != 0:
      result += j - flag 
      flag = 0


print(result)