import sys
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 각 원소의 부모를 자기 자신으로 초기화
        self.rank = [0] * n  # 트리의 높이를 관리하는 랭크 배열
        self.size = [1] * n  # 각 원소의 트리 크기를 관리하는 크기 배열

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # 랭크가 작은 트리를 큰 트리 밑에 붙이기 (트리 합치기)
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # 랭크를 증가시킴
                self.size[rootX] += self.size[rootY]
    def get_size(self,x):
        return self.size[self.find(x)]
    
# 예시 사용
# input() 대신 sys.stdin.readline 사용
n = int(sys.stdin.readline())
uf = UnionFind(10**6 + 1)

for _ in range(n): # n번 반복
    # sys.stdin.readline()으로 한 줄을 읽고, .split()으로 공백 분리, .strip()으로 개행 문자 제거
    inp = sys.stdin.readline().split() 

    if inp[0] == "I":
        # 정수 변환 시에도 int() 사용
        uf.union(int(inp[1]), int(inp[2]))
    else:
        print(uf.get_size(int(inp[1])))