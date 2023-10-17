import sys 
input = sys.stdin.readline

inf = int(1e9)
N = int(input())

roads = [list(map(int,input().split())) for _ in range(N)]
dp = [[inf]*(1<<N) for _ in range(N)]

def track(cur, visited):
    if visited == (1<<N) -1:
        return roads[cur][0] if roads[cur][0] else inf-1
    if dp[cur][visited] != inf:
        return dp[cur][visited]
    for i in range(1,N):
        if not roads[cur][i]:
            continue
        if visited & (1 << i):
            continue 
        dp[cur][visited] = min(dp[cur][visited],track(i,visited|(1<<i)) + roads[cur][i])
    
    if dp[cur][visited] == inf:
        return inf-1
    return dp[cur][visited]

print(track(0,1))



