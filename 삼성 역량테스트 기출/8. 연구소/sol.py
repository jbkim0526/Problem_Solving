import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())

b = [list(map(int,input().split()))for _ in range(n)]

coords = [(i,j) for j in range(m) for i in range(n) if b[i][j] == 0]
count_1 = sum([1 for j in range(m) for i in range(n) if b[i][j] == 1]) + 3
base_count = n*m-count_1
directions = [(0,1),(1,0),(0,-1),(-1,0)]

answer = 0
for c1,c2,c3 in combinations(coords,3):
    i1,j1 = c1 
    i2,j2 = c2
    i3,j3 = c3
    b[i1][j1] = 1 
    b[i2][j2] = 1 
    b[i3][j3] = 1 
    
    visited = set()
    count = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] != 2:
                continue 
            if (i,j) in visited:
                continue
            
            q = [(i,j)]
            while len(q) > 0:
                ci,cj = q.pop(0)
                if (ci,cj) in visited:
                    continue
                count += 1
                visited.add((ci,cj))
                for di,dj in directions:
                    ni,nj = ci+di,cj+dj
                    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1 or b[ni][nj] == 1:
                        continue
                    q.append((ni,nj))

    answer = max(answer, base_count-count)
    b[i1][j1] = 0 
    b[i2][j2] = 0 
    b[i3][j3] = 0 

print(answer)


