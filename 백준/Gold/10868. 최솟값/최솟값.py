import math

def set_tree_min(tree,idx):
    for i in range(idx,1,-1) :
        tree[i//2] = min(tree[i//2],tree[i])
    return

def min_tree(tree,start,end):
    result = []
    while start <= end :
        if start%2 == 1: result.append(tree[start])
        if end%2 == 0 : result.append(tree[end])
        start = (start+1)//2
        end = (end-1)//2
        
    print(min(result))
    return

n,m = map(int, input().split())
a = [int(input()) for _ in range(n)]
reqs = [list(map(int, input().split())) for _ in range(m)]

start_idx = 2**math.ceil(math.log2(n))
tree_size = start_idx*2
tree = [float('inf') for _ in range(10**7)]
tree[start_idx:tree_size] = a

set_tree_min(tree,start_idx + n )
for req in reqs:
    min_tree(tree,req[0] + start_idx-1 ,req[1] + start_idx - 1)
