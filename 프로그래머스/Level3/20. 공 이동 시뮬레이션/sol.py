def solution(n, m, x, y, queries):
    total_dx = 0
    total_dy = 0
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    for d, magnitude in queries:
        dx,dy = directions[d]
        total_dx += dx*magnitude
        total_dy += dy*magnitude
    print(total_dx, total_dy)
    if 0 < x < n-1 and 0 < y < m-1:
        return 1 if 0<=x-total_dx<=n-1 and 0<=y-total_dy<=m-1 else 0
    elif x == 0 and 0<y<m-1:
        return min(n,1-total_dx)if 0 <= y-total_dy <= m-1 and total_dx <= 0 else 0
    elif x == n-1 and 0<y<m-1:
        return min(n,1+total_dx) if 0 <= y-total_dy <= m-1 and total_dx >= 0 else 0
    elif y == 0 and 0<x<n-1:
        return min(m,1-total_dy) if 0 <= x-total_dx <= n-1 and total_dy <=0 else 0 
    elif y == m-1 and 0<x<n-1:
        return min(m,1+total_dy) if 0 <= x-total_dx <= n-1 and total_dy >=0 else 0 
    elif x==0 and y == 0 and total_dx <= 0 and total_dy <= 0:
        return min(n,1-total_dx)*min(m,1-total_dy)
    elif x==n-1 and y == m-1 and total_dx >= 0 and total_dy >=0:
        return min(n,1+total_dx)*min(m,1+total_dy)
    elif x== 0 and y == m-1 and total_dx <= 0 and total_dy >=0:
        return min(n,1-total_dx)*min(m,1+total_dy)
    elif x == n-1 and y == 0 and total_dx >= 0 and total_dy <= 0:
        return min(n,1+total_dx)*min(m,1-total_dy)

print(solution(4, 3, 2, 2, [[1,5],[2,-3]]))