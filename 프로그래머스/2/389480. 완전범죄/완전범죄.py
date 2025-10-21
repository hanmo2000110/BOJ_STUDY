def solution(info, n, m):
    answer = 1000000000
    k = len(info)
    check = set()

    def search(a_cnt, b_cnt, i = 0):   
        nonlocal answer, n, m

        if a_cnt >= n or b_cnt >= m: # 범위 이상이면 실패니까 그만 탐색
            return

        if (a_cnt, b_cnt, i) in check:
            return

        # 훔친 보물은 CHECK에 넣어서 다른 경우를 보지 않도록 함
        check.add((a_cnt, b_cnt, i))

        # 잡히지 않고 보물을 다 훔쳤으면 answer값을 a_cnt로 변경
        if i == k: 
            answer = min(answer, a_cnt)
            return 


        na = a_cnt + info[i][0]
        nb = b_cnt + info[i][1]

        search(na, b_cnt, i + 1) # a가 물건 훔친 경우
        search(a_cnt, nb, i + 1) # b가 물건 훔친 경우

    search(0, 0)

    if answer >= n:
        return -1
    else:
        return answer