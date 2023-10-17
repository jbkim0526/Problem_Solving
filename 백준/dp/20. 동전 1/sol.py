import sys 
input = sys.stdin.readline 

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

dp = [1] + [0 for _ in range(K)]

for coin in coins:
    for i in range(coin,K+1):
        dp[i] += dp[i-coin]

print(dp[K])





