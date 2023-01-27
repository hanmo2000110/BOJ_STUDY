from sys import stdin


def dfs(node, m, target):
    if m == target:
        global maxNode
        maxNode = node
        # print("maxNode :", maxNode)
    if node in check:
        return m

    check.add(node)
    # print(node)
    result = m

    for i in near[node]:
        if i in check:
            continue
        result = max(result, dfs(i, m + near[node][i], target))
    return result


v = int(input())
nodes = [list(map(int, stdin.readline().split())) for _ in range(v)]
near = [{} for _ in range(v+1)]
lastNodes = []

result = 0

for node in nodes:
    if len(node) == 4:
        lastNodes.append(node[0])
    for i in range(1, len(node)-1, 2):
        near[node[0]][node[i]] = node[i + 1]

maxNode = -1
# print(near)
# for i in range(len(near)):
#     print(i, ":", near[i])

# print("lastNode[0] : ", lastNodes[0])

check = set()
result = max(dfs(lastNodes[0], 0, -1), result)

check = set()
dfs(lastNodes[0], 0, result)

check = set()
result = max(dfs(maxNode, 0, -1), result)

# check = set()
# dfs(maxNode, 0, result)

print(result)
