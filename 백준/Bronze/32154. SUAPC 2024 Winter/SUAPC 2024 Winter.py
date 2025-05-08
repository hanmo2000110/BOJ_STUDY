# 백준 #32154 SUAPC 2024 Winter 브론즈 5

# 입력 ) N
N = int(input())
# print("입력된 등수 :",N)

# 스코어보드 2차원 리스트
Score_Board = [
    [11,["A","B","C","D","E","F","G","H","J","L","M"]], # 1등 AKARAKA
    [9,["A","C","E","F","G","H","I","L","M"]], # 2등 goraani
    [9,["A","C","E","F","G","H","I","L","M"]], # 3등 Raa_FanClub
    [9,["A","B","C","E","F","G","H","L","M"]], # 4등 입대 전 라스트 댄스
    [8,["A","C","E","F","G","H","L","M"]], # 5등 진짜 1등하러 왔습니다
    [8,["A","C","E","F","G","H","L","M"]], # 6등 돈비고고
    [8,["A","C","E","F","G","H","L","M"]], # 7등 가지오이당근
    [8,["A","C","E","F","G","H","L","M"]], # 8등 병공병
    [8,["A","C","E","F","G","H","L","M"]], # 9등 기령손
    [8,["A","B","C","F","G","H","L","M"]] # 10등 홍하예프
]

print(Score_Board[N-1][0])
# 푼 문제는 반복문을 활용하여 출력할 수 있음
Each_Elements = Score_Board[N-1][1]
# print(Each_Elements)

for letter in Each_Elements:
    print(letter, end=" ")
# 출력 1) N등을 한 팀이 푼 문제 수 출력
# 출력 2) N등을 한 팀이 푼 문제 번호를 사전 순으로 공백으로 구분하여 출력 (문제 번호의 알파벳은 대문자)