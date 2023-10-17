import sys 
from math import inf
input = sys.stdin.readline 

N = int(input())
roads = [list(map(int,input().split())) for _ in range(N)]
dp = [[(inf,[])]*(1<<N) for _ in range(N)]

for start in range(N):
    cur_dp = dp[start]
    cur_dp[0] = (0,[start])
    for i in range(1<<N):
        cur_cost, befores = cur_dp[i]
        k = 0
        for j in range(N):
            if i & (1<<j):
                k += 1
        for j in range(N):
            if k < N-1 and j == start:
                continue
            if i & (1<<j):
                continue
            res = []
            min_cost = cur_dp[i|(1<<j)][0]
            for before in befores:
                if roads[before][j] == 0:
                    continue
                if min_cost > cur_cost + roads[before][j]:
                    min_cost = cur_cost + roads[before][j]
                    res = [j]
                elif min_cost == cur_cost + roads[before][j]:
                    res.append(j)
            cur_dp[i|(1<<j)] = (min_cost,res)
            
ans = []
for start in range(N):
    ans.append(dp[start][-1][0])

print(min(ans))




