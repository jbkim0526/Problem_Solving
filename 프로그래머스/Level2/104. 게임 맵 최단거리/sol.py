from math import inf
def solution(maps):

    m, n = len(maps), len(maps[0])
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    grid = [[inf for _ in range(n)] for _ in range(m)]
    grid[0][0] = 1
    l = [(0,0)]

    while len(l) > 0:
        i,j = l.pop(0)
        for di,dj in directions:
            ni = i+di ; nj = j+dj
            if 0<=ni<=m-1 and 0<=nj<=n-1 and maps[ni][nj] == 1:
                if grid[i][j] + 1 < grid[ni][nj]:
                    grid[ni][nj] = grid[i][j] + 1
                    l.append((ni,nj))
                    
    if grid[m-1][n-1] == inf:
        return -1
    else:
        return grid[m-1][n-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))