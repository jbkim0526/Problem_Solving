from itertools import product
from copy import deepcopy
from math import inf

def solution(clockHands):

    answer = inf
    n = len(clockHands)
    directions = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]

    def rotate(i,j,rotate,grid):
        for di,dj in directions:
            if 0<=i+di<=n-1 and 0<=j+dj<=n-1:
                grid[i+di][j+dj] = (grid[i+di][j+dj] + rotate) % 4 
        return rotate

    for rotate_row in product([i for i in range(4)],repeat= n):
        grid = deepcopy(clockHands) 
        count = 0
        for j,r in enumerate(rotate_row):
            if r != 0:
                count += rotate(0,j,r,grid)
        for row in range(1,n):
            for col in range(n):
                if grid[row-1][col] != 0:
                    count += rotate(row, col, 4-grid[row-1][col], grid)
        if not any(grid[n-1]):
            answer = min(answer,count)

    return answer


print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))