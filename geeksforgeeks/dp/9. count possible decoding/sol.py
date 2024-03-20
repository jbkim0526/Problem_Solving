def CountWays(self, str):
    # Code here
    
    
    # dp[i]: index i 까지 고려했을 때 가능한 경우의 수
    # dp[i] 에서 i+1,i+2로 확장하는 방식
    
    n = len(str)
    limit = 26
    
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(n):
        
        if i+1 <=n:
            dp[i+1] += dp[i] % 1000000007 if str[i] != "0" else 0
            
        
        if i+2 <= n and int(str[i:i+2]) <= limit:
            dp[i+2] += dp[i] % 1000000007 if str[i] != "0" else 0
            
    return dp[n] % 1000000007