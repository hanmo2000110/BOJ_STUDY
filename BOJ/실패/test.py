def solution(cap, n, deliveries, pickups):
    answer = 0
    nd = n-1
    np = n-1

    while np >= 0 and nd >= 0:
        box = cap
        r = max(nd, np)
        answer += (r+1) * 2
        # print(answer, nd, np, box)
        while box != 0 and nd >= 0:
            # print(nd, deliveries[nd])
            if box > deliveries[nd]:
                box -= deliveries[nd]
                nd -= 1
            elif box == deliveries[nd]:
                nd -= 1
                break
            else:
                deliveries[nd] -= box
                break

        box = 0

        while box != cap and np >= 0:
            # print(np, pickups[np])

            if cap - box > pickups[np]:
                box += pickups[np]
                np -= 1
            elif cap - box == pickups[np]:
                np -= 1
                break
            else:
                pickups[np] -= cap - box
                break

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
