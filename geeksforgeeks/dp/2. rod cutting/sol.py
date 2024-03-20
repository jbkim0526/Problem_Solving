def cutRod(self, price, n):
    #code here
    dp = [0]*(n+1)
    dp[1] = price[0]
    
    for i in range(2,n+1):
        max_val =-1
        for rod in range(1,i+1):
            max_val = max(max_val, dp[i-rod] + price[rod-1])
        dp[i] = max_val
    return dp[n]