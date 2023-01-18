from collections import deque

n = int(input())
l = list(map(int, input().split()))

stack = deque()
result = ['-1'] * n
i = 1
stack.append(0)

while True:
    if i >= n:
        break
    while len(stack) != 0:
        t = stack.pop()
        if l[t] < l[i]:
            result[t] = str(l[i])
        else:
            stack.append(t)
            break
    stack.append(i)
    i += 1

print(" ".join(result))
# for i in count:
#     print(-1, end=" ")

'''
오큰수
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	54457	18309	13139	32.635%
문제
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

예제 입력 1 
4
3 5 2 7
예제 출력 1 
5 7 7 -1
예제 입력 2 
4
9 5 4 8
예제 출력 2 
-1 8 8 -1

접근법 :
왼쪽부터 시작해서 배열을 탐색하며 i번째 숫자보다 큰 수가 나오면 출력한다
만약 i+1, i+2 탐색하다 i번째 숫자보다 크지 않다면 그러한 숫자가 나온 횟수를 저장해둔다.
그리고 i번째 수보다 큰 수가 발견되면 그 수만큼 출력한다.
는 틀렸다

이걸 어떻게 풀지



'''
