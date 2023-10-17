def solution(scores):

    n = len(scores)
    target_score = scores[0]
    scores.sort(key = lambda x: (x[0],x[1]))
    maxa, maxb = scores[-1][0],scores[-1][1]
    l = []
    for i in range(n-1,-1,-1):
        if scores[i][0] == maxa or scores[i][1] >= maxb:
            l.append(scores[i])

    l.sort(key = lambda x: (x[1],x[0]))
    maxb, maxa = l[-1][1], l[-1][0]
    l2 = []
    for i in range(len(l)-1,-1,-1):
        if l[i][1] == maxb or l[i][0] >= maxa:
            l2.append(l[i])
    if target_score not in l2:
        return -1
    else:
        target_score = target_score[0] + target_score[1]
        for i in range(len(l2)):
            l2[i] = l2[i][0]+l2[i][1]
        l2.sort(reverse= True)
        return l2.index(target_score) + 1

#print(solution([[2,3],[1,4],[0,1000],[3,2],[5,0]]))
print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))