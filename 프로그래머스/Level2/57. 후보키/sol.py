from itertools import combinations

def solution(relation):
    answer = 0
    num_row, num_col = len(relation), len(relation[0])
   
    l = [i for i in range(num_col)]
    candidate_keys = []

    for n in range(1,num_col+1):
        for col in combinations(l, n):
            needCheck = True
            for key in candidate_keys:
                if set(key) <= set(col):
                    needCheck = False
                    break
            if not needCheck: continue
            s = set()
            for i in range(num_row):
                t = tuple()
                for j in col: t += (relation[i][j],)
                if t in s: break 
                else: s.add(t)
            else:
                answer += 1
                t = tuple()
                for i in col: t += (i,)
                candidate_keys.append(t)
    return answer



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))