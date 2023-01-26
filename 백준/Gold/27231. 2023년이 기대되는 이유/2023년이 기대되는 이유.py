def printCombinations(input, index, output, outLength):
    if (len(input) == index):
        output[outLength] = '\0'
        global l
        l.append(sum(list(map(int, "".join(output[:outLength]).split()))))
        return

    output[outLength] = input[index]

    output[outLength + 1] = ' '
    printCombinations(input, index + 1,
                      output, outLength + 2)

    if (len(input) != (index + 1)):
        printCombinations(input, index + 1,
                          output, outLength + 1)


t = int(input())
ts = [input() for i in range(t)]

for n in ts:
    l = []
    output = [0]*513
    output[0] = '\0'
    printCombinations(n, 0, output, 0)

# print(sorted(l))
    x = 1
    count = 0
    while True:
        s = 0
        for j in range(len(n)):
            s += int(n[j])**x
# print("s : ", s)
        x += 1
        if x > 100:
            # print("x : ", x)
            break
        if s in l:
            count += 1
    if count > 5:
        print("Hello, BOJ 2023!")
    else:
        print(count)
