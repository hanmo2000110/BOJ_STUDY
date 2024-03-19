import sys
input = sys.stdin.readline
 
def dfs(va,vb,vc) :
    
    if sum([va,vb,vc]) != c or (va,vb,vc) in check or va > a or vb > b or vc > c or va < 0 or vb < 0 or vc < 0:
        return
    # print("test : ", va,vb,vc)
    if va == 0 and vc not in result :
        
        result.append(vc)
        
    check.append((va,vb,vc))
    
    dfs(0,vb + va ,vc)
    dfs(0,vb ,vc+ va)
    dfs(va + vb,0,vc)
    dfs(va,0 ,vc+ vb)
    dfs(va,vb + vc,0)
    dfs(va + vc,vb ,0)
    
    dfs(va - (b - vb),b,vc)
    dfs(va- (c - vc),vb,c)
    dfs(a,vb- (a - va),vc)
    dfs(va,vb- (c - vc),c)
    dfs(a,vb,vc- (a - va))
    dfs(va,b,vc- (b - vb))
    
    
 
a,b,c = map(int ,input().split())
vA,vB,vC = (0,0,c)
result = []
check = []

dfs(vA,vB,vC)

print(" ".join(list(map(str, sorted(result)))))
