import sys 
from math import inf
input = sys.stdin.readline

n,m = map(int, input().split())
map = [[i for i in input()[:-1]] for _ in range(n)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
ri,rj,bi,bj,hi,hj = -1,-1,-1,-1,-1,-1

for i in range(n):
    for j in range(m):
        if map[i][j] == "R":
            ri,rj = i,j 
        elif map[i][j] == "B":
            bi,bj = i,j 
        elif map[i][j] == "O":
            hi,hj = i,j

dp = dict()

def slide(i,j,di,dj):
    while True:
        i,j = i+di,j+dj
        if i < 0 or i > n-1 or j < 0 or j > m-1:
            return i-di,j-dj
        if map[i][j] == "#":
            return i-di,j-dj
        if map[i][j] == "O":
            return i,j

def track(ri,rj,bi,bj,paths):

    if ri == hi and rj == hj:
        return 0
    
    if (ri,rj,bi,bj) in dp:
        return dp[(ri,rj,bi,bj)]
    
    if (ri,rj,bi,bj) in paths:
        return inf
    
    candidates = []
    paths.add((ri,rj,bi,bj))

    for di,dj in directions:

        nri,nrj = slide(ri,rj,di,dj)
        nbi,nbj = slide(bi,bj,di,dj)

        if nbi == hi and nbj == hj:
            continue

        if nri == nbi and nrj == nbj:
            if di == -1:
                if ri < bi : nbi += 1
                else: nri += 1
            elif di == 1:
                if ri > bi: nbi -= 1
                else: nri -= 1
            elif dj == -1:
                if rj < bj : nbj += 1
                else: nrj += 1
            elif dj == 1:
                if rj > bj : nbj -= 1
                else: nrj -= 1

        map[ri][rj],map[bi][bj],map[nri][nrj],map[nbi][nbj]  = ".",".","R","B"
        candidates.append(track(nri,nrj,nbi,nbj,paths)+1)
        map[ri][rj],map[bi][bj],map[nri][nrj],map[nbi][nbj],map[hi][hj]  = "R","B",".",".","O"
    ans = min(candidates)
    dp[(ri,rj,bi,bj)] = ans
    return ans

res = track(ri,rj,bi,bj,set())
res = res if res <= 10 else -1
print(res)

