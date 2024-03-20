def noOfWays(self, M, N, X):
    # code here

    dp = [[0 for _ in range(X+1)]for _ in range(N)]
    
    for i in range(1,min(X,M)+1):
        dp[0][i] = 1
    
    for dice_num in range(1,N):
        for total_val in range(1,X+1):
            for dice_val in range(1,M+1):
                if total_val-dice_val > 0:
                    dp[dice_num][total_val] += dp[dice_num-1][total_val-dice_val]  
                

    return dp[N-1][X]