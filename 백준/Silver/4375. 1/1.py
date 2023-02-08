try:
    while True:
        n = int(input())
        num = "1"
        while True:
            if int(num) % n == 0:
                print(len(num))
                break
            num += "1"
except Exception as e:
    exit()
