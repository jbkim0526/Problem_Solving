import sys 
from math import inf
sys.setrecursionlimit(1000000)
input = sys.stdin.readline 

n,m = map(int, input().split())
w = [list(map(int, input().split()))for i in range(n)]
directions = [(1,0),(0,1),(0,-1)]
dp = [[[inf,inf,inf] for _ in range(m)] for _ in range(n)]

def track(cx,cy,d):
    if dp[cx][cy][d] != inf:
        return dp[cx][cy][d]

    if cx == n-1:
        ans = sum(w[n-1][cy:])
        dp[cx][cy][d] = ans
        return ans
    
    answers = []
    for nd in range(3):
        if d == 1 and nd == 2:
            continue
        if d == 2 and nd == 1:
            continue
        dx,dy = directions[nd]
        nx,ny = cx+dx,cy+dy 
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue
        answers.append(track(nx,ny,nd) + w[cx][cy]) 

    ans = max(answers)
    dp[cx][cy][d] = ans
    return ans 

track(0,0,-1)

print(dp[0][0][-1])




