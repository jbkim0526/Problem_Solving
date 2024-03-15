import sys
from math import inf
input = sys.stdin.readline 

n = int(input())
dp = [inf]*(n+1)

dp[1] = 0

for i in range(1,n+1):
    if 3*i <= n:
        dp[3*i] = min(dp[3*i], dp[i]+1)
    if 2*i <= n:
        dp[2*i] = min(dp[2*i], dp[i]+1)
    if i+1 <= n:
        dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[n])