import sys 
from math import inf
input = sys.stdin.readline 

n,m = map(int, input().split())
w = [list(map(int, input().split()))for i in range(n)]


left = [[-inf for _ in range(m)] for _ in range(n)]
right = [[-inf for _ in range(m)] for _ in range(n)]
dp = [[-inf for _ in range(m)] for _ in range(n)]

dp[0][0] = w[0][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1] + w[0][i]

for i in range(1,n):

    left[i][0] = dp[i-1][0] + w[i][0]
    right[i][m-1] = dp[i-1][m-1] + w[i][m-1]

    for j in range(1,m):
        left[i][j] = max(dp[i-1][j],left[i][j-1]) + w[i][j]
    
    for j in range(m-2,-1,-1):
        right[i][j] = max(dp[i-1][j],right[i][j+1]) + w[i][j]
    
    for j in range(m):
        dp[i][j] = max(left[i][j],right[i][j])

print(dp[n-1][m-1])