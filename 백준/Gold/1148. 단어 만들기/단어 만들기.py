import sys

input_func = sys.stdin.readline
input_words = []

while True:
    word = input_func().rstrip()
    if word == '-':
        break
    input_words.append(word)

while True:
    board = input_func().rstrip()
    letter_count = [0] * 26
    if board == '#':
        break
    board_letter_count = [0] * 26
    for letter in board:
        board_letter_count[ord(letter) - 65] += 1

    for input_word in input_words:
        word_letter_count = [0] * 26
        for letter in input_word:
            word_letter_count[ord(letter) - 65] += 1
        flag = True
        for i in range(26):
            if board_letter_count[i] < word_letter_count[i]:
                flag = False
        if flag:
            for letter in set(input_word):
                letter_count[ord(letter) - 65] += 1

    min_count = 10**9
    min_list = []
    max_count = 0
    max_list = []

    for letter in set(board):
        count = letter_count[ord(letter) - 65]
        if min_count == count:
            min_list.append(letter)
        elif count < min_count:
            min_count = count
            min_list = [letter]
        if max_count == count:
            max_list.append(letter)
        elif count > max_count:
            max_count = count
            max_list = [letter]
    print(''.join(sorted(min_list)), min_count, ''.join(sorted(max_list)), max_count)
