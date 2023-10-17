from math import inf

def solution(alp, cop, problems):
    alp_max,cop_max = -1,-1

    for p in problems:
        alp_max = max(alp_max,p[0])
        cop_max = max(cop_max,p[1])

    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])

    alp,cop = min(alp,alp_max),min(cop,cop_max)
    dp = [[inf for _ in range(cop_max+1)] for _ in range(alp_max+1)]
    dp[alp][cop] = 0

    for i in range(alp,alp_max+1):
        for j in range(cop,cop_max+1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue 
                ni,nj = min(i+alp_rwd,alp_max), min(j+cop_rwd,cop_max)
                dp[ni][nj] = min(dp[ni][nj],dp[i][j]+cost)

    return dp[alp_max][cop_max]


print(solution(	0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))