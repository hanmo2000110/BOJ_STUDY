def check(array, target, num):
    count = 0
    for n in array:
        count += n // num
    if count >= target:
        count = 0
        for n in array:
            count += n // (num+1)
        if count >= target:
            return 1
        else:
            return 0
    else:
        return -1


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    result = check(array, target, mid)

    if result == 0:
        return mid
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif result == -1:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    elif result == 1:
        return binary_search(array, target, mid + 1, end)


k, n = map(int, input().split())
l = [int(input()) for i in range(k)]

print(binary_search(l, n, 1, max(l)))
