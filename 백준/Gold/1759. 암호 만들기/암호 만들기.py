def is_valid(password):
    vowels = set('aeiou')
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def backtrack(start, password, L, C, characters, results):
    if len(password) == L:
        if is_valid(password):
            results.append(password)
        return
    
    for i in range(start, C):
        backtrack(i + 1, password + characters[i], L, C, characters, results)

def main():
    L, C = map(int, input().split())
    characters = sorted(input().split())
    results = []
    
    backtrack(0, '', L, C, characters, results)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()