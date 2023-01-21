"""
나무 자르기 실버2

접근법 : 
상근이가 나무를 M 가져가고 싶어하며 초과해서 가져가면 안된다.
제한시간은 1초이다
완전탐색 알고리즘으로 푼다면 1000000 * 2,000,000,000 
시간 복잡도를 무조건 초과하게 되어있다.
더욱 빠른 탐색 알고리즘인 이분탐색을 사용하겠다.
"""


def checkMeter(target, treeList):
    s = 0
    for tree in treeList:
        if tree > target:
            s += tree - target

    return s


def binary_search(start, end, target, treeList):

    if start > end or start == 7:
        return None

    mid = (end + start) // 2
    # print(start, end, target, treeList, mid,
    #       checkMeter(mid, treeList), checkMeter(mid+1, treeList))
    if checkMeter(mid, treeList) >= target and checkMeter(mid + 1, treeList) < target:
        return mid
    if checkMeter(mid, treeList) > target:
        return binary_search(mid+1, end, target, treeList)
    else:
        return binary_search(start, mid-1, target, treeList)


n, m = map(int, input().split())
treeList = list(map(int, input().split()))

print(binary_search(0, max(treeList), m, treeList))
