def sol(n):
    n -= 1
    if n % 3 == 0:
        return "U"
    elif n % 3 == 1:
        return "O"
    elif n % 3 == 2:
        return "S"
 
 
if __name__ == '__main__':
    n = int(input())
    print(sol(n))