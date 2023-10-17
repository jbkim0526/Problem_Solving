from math import inf
from heapq import heappush,heappop

def solution(alp, cop, problems):
    answer = inf
    n = 30
    alp_max,cop_max = -1,-1

    for p in problems:
        alp_max = max(alp_max,p[0])
        cop_max = max(cop_max,p[1])
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])

    score = [[inf for _ in range(cop_max+n)] for _ in range(alp_max+n)]
    heap = []
    heappush(heap,(0,alp,cop))

    while len(heap) > 0:
        cur_score,cur_alp,cur_cop = heappop(heap)
        if score[cur_alp][cur_cop] != inf:
          continue
        score[cur_alp][cur_cop] = cur_score
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if cur_alp < alp_req or cur_cop < cop_req:
                continue 
            alp_new = cur_alp + alp_rwd
            cop_new = cur_cop + cop_rwd 
            if alp_new > alp_max+n-1 or cop_new > cop_max+n-1:
                continue 
            new_score = cur_score + cost
            if score[alp_new][cop_new] <= cur_score + cost:
                continue 
            heappush(heap,(new_score,alp_new,cop_new))

    for i in range(alp_max,alp_max+n):
        for j in range(cop_max,cop_max+n):
            answer = min(answer,score[i][j])
    print(score)
    return answer


print(solution(	0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))