
def MinSquares(self, n):
    # Code here
    
    squares = [i*i for i in range(1,int(n**(1/2))+1)]
    inf = 1e6
    # dp[i]: 숫자 i를 만드는 최소 개수
    dp = [0]+[inf]*n
    
    
    for num in range(n+1):
        for square in squares:
            if num+square <= n:
                dp[num+square] = min(dp[num+square],dp[num]+1)
        
    return dp[n]