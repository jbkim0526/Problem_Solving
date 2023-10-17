from math import inf
import sys 
input = sys.stdin.readline 

N, M = map(int,input().split())
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))
sum_costs = sum(costs)

dp = [0]+[-1 for _ in range(sum_costs)]

for i in range(N):
    cost = costs[i]
    memory = memories[i]
    for j in range(sum_costs,cost-1,-1):
        if dp[j-cost] == -1:
            continue
        dp[j] = max(dp[j],dp[j-cost]+memory)

for i in range(sum_costs+1):
    if dp[i] < M:
        continue
    print(i)
    break
