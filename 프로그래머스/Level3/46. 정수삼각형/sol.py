def solution(triangle):
    n = len(triangle)
    directions = [(-1,0),(-1,-1)]
    dp = [[0 for _ in range(i+1)] for i in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,n):
        for j in range(i+1):
            before_vals = []
            for di,dj in directions:
                ni,nj = i+di,j+dj 
                if ni < 0 or nj < 0 or nj > i-1:
                    continue 
                else:
                    before_vals.append(dp[ni][nj])
            dp[i][j] = max(before_vals) + triangle[i][j]

    return max(dp[n-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))