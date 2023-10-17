def findmax(answers, l,n):
    candidates = []
    
    for elem in answers:
        count = 0
        temp = []
        for i in range(10):
            arrow = l[i][int(elem[i])]
            count += arrow 
            temp.append(arrow)
        temp.append(n-count)
        candidates.append(temp)

    max_tuple = (0,0,0,0,0,0,0,0,0,0,0)
    max_index = 0
    for i,elem in enumerate(candidates):
        t = tuple(reversed(elem)) 
        if t > max_tuple:
            max_tuple = t 
            max_index = i 
    return candidates[max_index]

def solution(n, info):
    answers = []
    l = []
    maxscore = 0

    for i in range(10):
        elem = info[i]
        if elem == 0:
            l.append((0,1))
        else:
            l.append((0,elem+1))
    
    for i in range(2**10):
        s = bin(i)[2:].zfill(10)
        score = -1
        m = 0
        isimpossible = False
        for j in range(10):
            arrow = l[j][int(s[j])]
            if arrow != 0:
                m += arrow 
                if m > n:
                    isimpossible = True
                    break 
                else: 
                    score += 10-j
            else:
                if info[j] > 0:
                    score -= 10-j
        if isimpossible: 
            continue
        if score > maxscore:
            maxscore = score 
            answers = [s]
        elif score == maxscore:
            answers.append(s)


    if len(answers) == 0:
        return [-1]

    answer = findmax(answers, l,n)
    return answer

print(solution(5	,[2,1,1,1,0,0,0,0,0,0,0]))