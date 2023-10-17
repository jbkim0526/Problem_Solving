import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline 

N  = int(input())
M = int(input())

dp = [dict() for _ in range(M)]
cases = []
for _ in range(M):
    cases.append( list(map(int, input().split())))

def track(x1,y1,x2,y2,depth):

    if depth == M:
        return 0
    if (x1,y1,x2,y2) in dp[depth]:
        return dp[depth][(x1,y1,x2,y2)][0] 
    nx,ny = cases[depth]
    dists = []
    dists.append(track(nx,ny,x2,y2,depth+1)+abs(x1-nx)+abs(y1-ny))
    dists.append(track(x1,y1,nx,ny,depth+1)+abs(x2-nx)+abs(y2-ny))
    dist = min(dists)
    dp[depth][(x1,y1,x2,y2)] = (dist, 1 if dist == dists[0] else 2)

    return dist

track(1,1,N,N,0)
print(dp[0][(1,1,N,N)][0])
x1,y1 = 1,1
x2,y2 = N,N

for depth in range(M):
    police = dp[depth][(x1,y1,x2,y2)][1]
    print(police)
    if police == 1:
        x1,y1 = cases[depth]
    else:
        x2,y2 = cases[depth]