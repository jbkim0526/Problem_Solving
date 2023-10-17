def solution(matrix_sizes):
  
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
 
    for l in range(2, n+1):
        for i in range(0, n-l+1):
            
            j = i+l-1
            a = matrix_sizes[i][0]
            c = matrix_sizes[j][1]
            res = []

            for k in range(l-1):
                b = matrix_sizes[i+k][1]
                mul_count = a*b*c 
                if k == 0:
                    res.append(mul_count + dp[i+1][j])
                elif k == l-1:
                    res.append(mul_count + dp[i][j-1])
                else:
                    res.append(mul_count + dp[i][i+k]+dp[i+k+1][j])
                
            dp[i][j] = min(res)
            
    return dp[0][n-1]


print(solution([[5,3],[3,10],[10,6]]))