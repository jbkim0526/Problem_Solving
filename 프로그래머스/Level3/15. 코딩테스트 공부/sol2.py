from math import inf

def solution(alp, cop, problems):
    max_alp, max_cop = -1,-1
    for p in problems:
        max_alp = max(max_alp,p[0])
        max_cop = max(max_cop,p[1])
    
    if alp >= max_alp and cop >= max_cop:
        return 0

    elif alp >= max_alp:

        dp = [inf for _ in range(max_cop+1)]
        dp[cop] = 0
        for i in range(1,max_cop-cop+1):
            c = cop + i 
            l = []
            if c-1 >= cop: l.append(dp[c-1]+1)
            for p in problems:
                n_alp, n_cop, g_alp, g_cop, cost = tuple(p)
                if n_cop <= c-g_cop:
                    l.append(dp[c-g_cop]+cost)
            dp[c] = min(l)
        return dp[max_cop]

    elif cop >= max_cop:
        dp = [inf for _ in range(max_alp+1)]
        dp[alp] = 0
        for i in range(1,max_alp-alp+1):
            a = alp + i 
            l = []
            if a-1 >= alp: l.append(dp[a-1]+1)
            for p in problems:
                n_alp, n_cop, g_alp, g_cop, cost = tuple(p)
                if n_alp <= a-g_alp:
                    l.append(dp[a-g_alp]+cost)
            dp[a] = min(l)
        return dp[max_alp]

    else:
        m = max_alp+max_cop
        dp = [[inf for _ in range(m+1)] for _ in range(m+1)]
        dp[alp][cop] = 0

        for i in range(1,m+1-(alp+cop)):
            for j in range(i+1):
                
                a,c = alp+j, cop+i-j
                l = []
                if a-1 >= alp : l.append(dp[a-1][c]+1)
                if c-1 >= cop : l.append(dp[a][c-1]+1)

                for p in problems:
                    n_alp, n_cop, g_alp, g_cop, cost = tuple(p)
                    if n_alp <= a-g_alp and n_cop <= c-g_cop :
                        l.append(dp[a-g_alp][c-g_cop] + cost)
                dp[a][c] = min(l)
    return dp[max_alp][max_cop]

print(solution(10,100000,[[10,15,2,1,2],[20,20,3,3,4]]))
#print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
