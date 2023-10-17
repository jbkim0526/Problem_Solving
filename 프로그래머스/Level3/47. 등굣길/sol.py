def solution(m, n, puddles):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    directions = [(-1,0),(0,-1)]
    puddles_set = set()

    for a,b in puddles:
        puddles_set.add((a-1,b-1))

    for i in range(m):
        for j in range(n):
            if (i,j) in puddles_set:
                continue
            count = dp[i][j]
            for di,dj in directions:
                ni,nj = i+di,j+dj 
                if ni < 0 or nj < 0 or (ni,nj) in puddles_set:
                    continue 
                count += dp[ni][nj]
            dp[i][j] = count 

    return (dp[m-1][n-1] % 1000000007)




print(solution(4, 3, [[2, 2]]))