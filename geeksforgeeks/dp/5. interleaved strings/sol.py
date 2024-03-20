def isInterleave(self, A, B, C):
    # Code here

    #dp[i][j] : A의 i번째째, B의 j번째 까지 사용해서 C를 만들 수 있는지 여부
    
    size_a, size_b = len(A),len(B)
    
    if (size_a + size_b) != len(C):
        return 0
        
    dp = [[0 for _ in range(size_b+1)] for _ in range(size_a+1)]
    
    
    for i in range(size_a+1):
        for j in range(size_b+1):
            
            if i == 0 and j == 0: 
                dp[i][j] = 1
            
            elif i == 0 and B[j-1] == C[j-1]:
                dp[i][j] = dp[i][j-1]
            
            elif j == 0 and A[i-1] == C[i-1]:
                dp[i][j] = dp[i-1][j]
            
            elif dp[i-1][j] and A[i-1] == C[i+j-1]:
                dp[i][j] = 1
                
            elif dp[i][j-1] and B[j-1] == C[i+j-1]:
                dp[i][j] = 1



    return dp[size_a][size_b]