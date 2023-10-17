from collections import deque
import sys 
input = sys.stdin.readline 

m,n = map(int, input().split())
dp = [[0 for _ in range(n)] for _ in range(m)]
directions = [(-1,0),(0,-1),(0,1),(1,0)]
dp[0][0] = 1
grid = []

for i in range(m):
    grid.append(list(map(int, input().split())))

l = deque()
l.append((0,0))

while len(l) > 0:
    curi,curj = l.popleft()
    cur_height = grid[curi][curj]
    for di,dj in directions:
        ni,nj = curi+di,curj+dj
        if ni < 0 or ni > m-1 or nj < 0 or nj > n-1:
            continue 
        nheight = grid[ni][nj]
        if cur_height <= nheight:
            continue 
        dp[ni][nj] += 1
        l.append((ni,nj))


print(dp[m-1][n-1])