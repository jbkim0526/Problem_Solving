import sys
from math import inf
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[n] : n을 만들 수 있는 최소의 경우의 수
dp = [inf for _ in range(k+1)]
dp[0] = 0

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i-coin] + 1,dp[i])

print(dp[k] if dp[k] != inf else -1)


