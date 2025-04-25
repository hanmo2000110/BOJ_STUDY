import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

def insert(root, number):
    node = root
    for digit in number:
        if digit not in node.children:
            node.children[digit] = Node()
        node = node.children[digit]
        if node.is_end:  # 중간에 끝나는 번호가 있으면 일관성 없음
            return False
    if node.children:  # 현재 번호가 다른 번호의 접두사인 경우
        return False
    node.is_end = True
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    root = Node()
    consistent = True
    for num in sorted(numbers):  # 사실 정렬은 필수는 아님
        if not insert(root, num):
            consistent = False
            break
    print("YES" if consistent else "NO")
