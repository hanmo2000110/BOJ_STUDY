# 백준 #31654 (Adding Trouble)

## A, B, C 입력받기
A, B, C = input().split()

# 정수로 변환한 뒤 다시 저장
A = int(A)
B = int(B)
C = int(C)

## 만약 A + B = C ==> correct! 출력
## 만약 A + B /= C ==> wrong! 출력 
if A + B == C :
    print("correct!")
else :
    print("wrong!")