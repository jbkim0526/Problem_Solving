def solution(n, m, x, y, queries):
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    start_set = set([(x,y)])
    len_queries = len(queries)
    for i in range(len_queries-1,-1,-1):
        d, magnitude = queries[i]
        dx = directions[d][0] * magnitude
        dy = directions[d][1] * magnitude
        new_set = set()
        for x,y in start_set:
            if 0 < x < n-1 and 0 < y < m-1 and 0<=x-dx<=n-1 and 0<=y-dy<=m-1:
                new_set.add((x-dx,y-dy))
            elif x == 0 and 0<y<m-1 and 0 <= y-dy <= m-1 and dx <= 0:
                new_set.update([(i,y-dy) for i in range(min(n,1-dx))])
            elif x == n-1 and 0<y<m-1 and 0 <= y-dy <= m-1 and dx >= 0:
                new_set.update([(i,y-dy) for i in range(n-min(n,1+dx),n)])
            elif y == 0 and 0<x<n-1 and 0 <= x-dx <= n-1 and dy <=0 :
                new_set.update([(x-dx,j) for j in range(min(m,1-dy))])
            elif y == m-1 and 0<x<n-1 and 0 <= x-dx <= n-1 and dy >=0:
                new_set.update([(x-dx,j) for j in range(m-min(m,1+dy),m)])
            elif x==0 and y == 0 and dx <= 0 and dy <= 0:
                new_set.update([(i,j) for i in range(min(n,1-dx)) for j in range(min(m,1-dy))])
            elif x==n-1 and y == m-1 and dx >= 0 and dy >=0:
                new_set.update([(i,j) for i in range(n-min(n,1+dx),n) for j in range(m-min(m,1+dy),m)])
            elif x== 0 and y == m-1 and dx <= 0 and dy >=0:
                new_set.update([(i,j) for i in range(min(n,1-dx)) for j in range(m-min(m,1+dy),m)])
            elif x == n-1 and y == 0 and dx >= 0 and dy <= 0:
                new_set.update([(i,j) for i in range(n-min(n,1+dx),n) for j in range(min(m,1-dy))])
        start_set = new_set
        new_set = set()
    return len(start_set)