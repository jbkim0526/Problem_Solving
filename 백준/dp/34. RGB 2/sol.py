import sys 
from math import inf
input = sys.stdin.readline 

n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]
ans = inf

for k in range(3):
    a,a1,a2 = k,(k+1)%3,(k+2)%3
    dp = [[inf,inf,inf] for _ in range(n)]
    dp[0][a] = costs[0][a]

    for i in range(1,n):
        if i != n-1:
            dp[i][a] = min(dp[i-1][a1],dp[i-1][a2])+ costs[i][a]
        dp[i][a1] = min(dp[i-1][a],dp[i-1][a2])+ costs[i][a1]
        dp[i][a2] = min(dp[i-1][a],dp[i-1][a1])+ costs[i][a2]

    ans = min(ans,min(dp[n-1]))

print(ans)