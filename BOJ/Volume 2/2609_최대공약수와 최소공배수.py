'''
최대공약수와 최소공배수 브론즈1

이미 최대공약수와 최대공배수를 구하는 함수가 Math 라이브러리에 구현되어있다
'''

import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
