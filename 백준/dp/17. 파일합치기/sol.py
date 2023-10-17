from math import inf
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    sizes = list(map(int,input().split()))
    
    dp = [[0 for j in range(n)] for i in range(n)]
    add_results = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        add_result = 0
        for j in range(i,n):
            add_result += sizes[j]
            add_results[i][j] = add_result
            
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            res = []
            for k in range(1,l):
                res.append(dp[i][i+k-1]+dp[i+k][j]+add_results[i][j])  
              
            dp[i][j] = min(res)
    print(dp[0][n-1])
 

