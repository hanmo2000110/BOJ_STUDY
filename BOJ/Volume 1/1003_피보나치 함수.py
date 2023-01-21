'''
피보나치 함수 실버3
https://www.acmicpc.net/problem/1003
다이나믹 프로그래밍

접근법 :
디피로 각 피보나치마다 0과 1이 호출된 횟수를 계산한다 

점화식 :
a0[0] = 1
a0[1] = 0
a0[i] = a0[i-1] + a0[i-2]

a1[0] = 0
a1[1] = 1
a1[i] = a1[i-1] + a[i-2]
'''

t = int(input())
l = [int(input()) for i in range(t)]

a0 = [0] * 41
a1 = [0] * 41
a0[0] = 1
a0[1] = 0
a1[0] = 0
a1[1] = 1
for i in range(2, 41):
    a0[i] = a0[i-1] + a0[i-2]
    a1[i] = a1[i-1] + a1[i-2]

for x in l:
    print(a0[x], a1[x])
