def numTrees(self,N):
    # code here
    # dp[i] : 숫자 i개로 만드는 unique bst 개수
    dp = [0]*(N+1)
    dp[0] = 1
    
    # 1 부터 N까지
    for i in range(1,N+1):
        # j: root node의 번호
        for j in range(1,i+1):
            dp[i] += dp[j-1]*dp[i-j] % 1000000007  

    return dp[N] % 1000000007