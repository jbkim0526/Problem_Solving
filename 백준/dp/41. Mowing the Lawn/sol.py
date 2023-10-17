import sys 
from collections import deque
input = sys.stdin.readline 

n,k = map(int,input().split())
eff = [int(input()) for _ in range(n)]
dp = [0]*(n+1)
p_sum = [0]*(n+1)
d = deque()

for i in range(1,n+1):
    p_sum[i] = p_sum[i-1] + eff[i-1]

if n == k:
    print(p_sum[n])
else:
    for i in range(k+1):
        dp[i] = p_sum[i]
        d.append((i,dp[i]-p_sum[i+1]))

    for i in range(k+1,n+1):
        dp[i] = p_sum[i] + d[0][1]
        if i == n:
            break
        val = dp[i]-p_sum[i+1]
        while d and d[-1][1] < val: d.pop()
        while d and d[0][0] < i-k: d.popleft()
        d.append((i,val))

    print(dp[n])
    





