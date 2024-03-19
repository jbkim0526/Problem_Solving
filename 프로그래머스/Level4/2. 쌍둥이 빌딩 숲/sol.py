def nCk(n,k):
    res = 1
    div = 1
    for i in range(k):
        res *= (n-i)
        div *= (i+1)
    return res // div

def solution(n, count):

    # dp[i][j] : i개 빌딩이 있을 때 앞에서 j개만 보이는 경우의 수
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    dp[1][1] = 1
    sum_dp = [1,1] +[0]*(n-1)

    for i in range(2,n+1):
        for j in range(1,i+1):
            
            if j == 1:
                for k in range(i):
                    dp[i][j] += (nCk(i-1,i-1-k)*sum_dp[i-1-k]*sum_dp[k]) % 1000000007
                
            elif j == i:
                dp[i][j] = 1
            
            else:
                for k in range(1,i-j+2):
                    dp[i][j] += (nCk(i-1,k-1)*dp[i-k][j-1]*dp[k][1]) % 1000000007
        
        sum_dp[i] = sum(dp[i]) % 1000000007

    return dp[n][count] % 1000000007