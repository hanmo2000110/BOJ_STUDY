def backTracking(num, i,rt) :
    if i >= n:
        global result_max
        global result_min
        result_max = max(result_max,num)
        result_min = min(result_min,num)

        return
    
    global plus
    global minus
    global mult
    global div

    if plus >= 1 :
        plus -= 1
        backTracking(num + nList[i],i+1,rt+"+ ")
        plus += 1
    if minus >= 1 :
        minus -= 1
        backTracking(num - nList[i],i+1,rt+"- ")
        minus += 1
    if mult >= 1 :
        mult -= 1
        backTracking(num * nList[i],i+1,rt+"* ")
        mult += 1
    if div >= 1 :
        div -= 1
        p = 1
        if (num < 0 or nList[i] < 0) and not (num < 0 and nList[i] < 0) : 
            p = -1
        backTracking( p * ( abs(num) // abs(nList[i])),i+1,rt+"/ ")
        div += 1


n = int(input())

nList = list(map(int, input().split()))

plus,minus,mult,div = map(int , input().split())

result_max = -1000000001
result_min = 1000000001


backTracking(nList[0] ,1,"")

print(int(result_max))
print(int(result_min))

