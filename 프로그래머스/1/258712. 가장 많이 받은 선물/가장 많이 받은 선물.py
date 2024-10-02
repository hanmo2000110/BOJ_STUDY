def solution(friends, gifts):
    answer = 0
    counting = {}
    result = {}
    l = {}
    
    for fr in friends :
        counting[fr] = 0
        result[fr] = 0
        l[fr] = {}
        for to in friends :
            if fr == to :
                continue
            l[fr][to] = 0

    for gift in gifts :
        relation = gift.split()
        
        counting[relation[0]] += 1
        counting[relation[1]] -= 1
        l[relation[0]][relation[1]] += 1
        
    
    print(l)
    
    for fr in friends :
        for to in friends :
            if fr == to :
                continue
                
            if l[fr][to] > l[to][fr] :
                result[fr] += 1
            elif l[fr][to] < l[to][fr] :
                result[to] += 1
            else :
                if counting[fr] > counting[to] :
                    result[fr] += 1
                elif counting[fr] < counting[to] :
                    result[to] += 1
    answer = 0
    for re in result :
        answer = max(answer, result[re]/2)
        # print(result)

    
    return answer