import sys

def dfs(start, current, visited, path):
    if current in visited:  # 이미 방문한 노드라면
        if current == start:  # 사이클이 완성된 경우
            result_set.update(path)  # 현재 경로의 모든 노드를 결과에 추가
        return
    
    visited.add(current)  # 현재 노드 방문 표시
    path.append(current)  # 현재 경로에 노드 추가
    dfs(start, numbers[current-1], visited, path)  # 다음 노드로 이동

N = int(sys.stdin.readline())
numbers = []
result_set = set()

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 각 노드에서 시작하여 사이클 찾기
for i in range(1, N+1):
    dfs(i, i, set(), [])

# 결과 출력
result = sorted(list(result_set))
print(len(result))
for num in result:
    print(num)