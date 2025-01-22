t = int(input())                     # 테스트 케이스를 입력 받기

for _ in range(t):                   # 테스트 케이스만큼 반복문 돌기
    arr = []                         # 순간 이동한 거리를 담는 배열(len를 출력하기 위해)
    a = 1                            # 한 번 순간 이동할 거리
    x, y = map(int,input().split())  # x, y 의 거리를 입력 받기
    distance = y - x                 # 총 이동할 거리
    while True:                      # 무한 루프
        for _ in range(2):           # 맨 앞과 맨 뒤, 총 두 번 a를 빼준다. 
            if distance <= a:        # 만약 남은 거리가 a 보다 작으면
                arr.append(distance) # 남은 거리를 리스트에 담기
                distance = 0         # 다 담았으면 거리는 0 남음
                break                # 남은 거리가 없으니 반복문 탈출
            distance = distance - a  # a 보다 거리가 크다면 빼라
            arr.append(a)            # 뺀 a는 순간 이동한 것이기에 리스트에 담아라
        a += 1                       # a는 1,2,3,4,5~ 이렇게 증가한다.
        if distance <= 0:            # 만약 거리가 0이거나 작을 경우
            break                    # 무한 루프 탈출
    print(len(arr))           