def solution(scores):

    n = len(scores)
    target_score = scores[0]
    scores.sort(key = lambda x: (x[0],x[1]))
    maxa = scores[-1][0]
    maxbs = [scores[-1][1]]
    maxb = scores[-1][1]
    l = []
    current_i = maxa
    for i in range(n-1,-1,-1):
        if scores[i][0] == maxa:
            l.append(scores[i])
        else:
            if scores[i][0] != current_i:
                current_i = scores[i][0]
                maxbs.append(scores[i][1])
                maxb = max(maxb, maxbs[-2])
            if scores[i][1] >= maxb:
                l.append(scores[i])
    if target_score not in l:
        return -1
    else:
        target_score = target_score[0] + target_score[1]
        for i in range(len(l)):
            l[i] = l[i][0]+l[i][1]
        l.sort(reverse= True)
        return l.index(target_score) + 1
    


#print(solution([[2,10],[1,11],[1,11],[1,11]]))
#print(solution([[2,3],[1,4],[3,3],[3,2],[2,1]]))
print(solution([[2,3],[1,4],[3,1000],[3,2],[5,0]]))