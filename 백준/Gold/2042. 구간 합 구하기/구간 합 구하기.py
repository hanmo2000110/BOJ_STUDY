import math

def set_tree(tree,idx):
    for i in range(idx,1,-1) :
        tree[i//2] += tree[i]
    return

def update_tree(tree,idx,to):
    tree[idx] = to
    while idx > 1 :
        idx = idx//2
        tree[idx] = tree[idx*2] + tree[idx*2+1]
    return

def find_tree(tree,start,end):
    result = []
    while start <= end :
        if start%2 == 1: result.append(tree[start])
        if end%2 == 0 : result.append(tree[end])
        start = (start+1)//2
        end = (end-1)//2
        
    print(sum(result))
    return

n,m,k = map(int, input().split())
a = [int(input()) for _ in range(n)]
reqs = [list(map(int, input().split())) for _ in range(m+k)]

start_idx = 2**math.ceil(math.log2(n))
tree_size = start_idx*2
tree = [0 for _ in range(10**7)]
tree[start_idx:tree_size] = a

set_tree(tree,start_idx + n )
for req in reqs:
    if req[0] == 1:
        update_tree(tree,req[1]+ start_idx - 1,req[2])
    else :
        find_tree(tree, req[1] + start_idx - 1, req[2] + start_idx - 1)


# print(tree[:tree_size])