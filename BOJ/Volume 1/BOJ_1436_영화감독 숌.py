'''
영화감독 숌 실버5
'''

x = int(input())

n = 0
count = 0

while count != x:
    if str(n).count("666") != 0:
        count += 1
    n += 1

print(n - 1)
