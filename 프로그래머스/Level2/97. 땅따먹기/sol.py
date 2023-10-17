def solution(land):
    n = len(land)
    dp = [land[0]]+[[0,0,0,0] for _ in range(n-1)]

    for i in range(1,n):
        for j in range(4):
            x,y,z = tuple(x for x in [0,1,2,3] if x != j)
            dp[i][j] = max(dp[i-1][x],dp[i-1][y],dp[i-1][z])+land[i][j]
    return max(dp[n-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))