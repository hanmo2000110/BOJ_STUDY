import sys
from collections import deque
input = sys.stdin.readline
 
def checkMid(word, target_word):
    target_word_idx = 0
    word_idx = 0
    while word_idx < len(word):
        if word[word_idx] == target_word[target_word_idx]:
            target_word_idx += 1
        word_idx += 1
    if target_word_idx == len(target_word):
        return True
    else : 
        return False
    

def bfs(start):
    global result 
    visited = []
    queue = deque([start])
    visited.append(start)
    # print(queue)
    while queue:
        target = queue.popleft()
        # print("inside while : ",target)
        
        for word in words:
            # print("inside for : ",word)
            if word in visited or len(word) - 1 != len(target) :
                continue
            
            # print(word[1:], word[:-1])
            
            if target in word or checkMid(word,target):
                queue.append(word)
                visited.append(word)
                
                result = word
            # print("result : ",result)
            # print("queue : ", queue)
        # print()

                

n, start = input().split()
n = int(n)
words = [input().rstrip() for _ in range(n)]
result = start

bfs(start)
print(result)



