
def solution(n, m, x, y, queries):
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    start_set = set([(x,y)])
    len_queries = len(queries)
    dp = {}
    for i in range(len_queries-1,-1,-1):
        d, magnitude = queries[i]
        dx = directions[d][0] * magnitude
        dy = directions[d][1] * magnitude
        new_set = set()
        for x,y in start_set:

            if (x,y,dx,dy) in dp:
                new_set.update(dp[(x,y,dx,dy)])
                continue
            l = []
            if 0 < x < n-1 and 0 < y < m-1 and 0<=x-dx<=n-1 and 0<=y-dy<=m-1:
                l.append((x-dx,y-dy))
            elif x == 0 and 0<y<m-1 and 0 <= y-dy <= m-1 and dx <= 0:
                l = [(i,y-dy) for i in range(min(n,1-dx))]
            elif x == n-1 and 0<y<m-1 and 0 <= y-dy <= m-1 and dx >= 0:
                l = [(i,y-dy) for i in range(n-min(n,1+dx),n)]
            elif y == 0 and 0<x<n-1 and 0 <= x-dx <= n-1 and dy <=0 :
                l = [(x-dx,j) for j in range(min(m,1-dy))]
            elif y == m-1 and 0<x<n-1 and 0 <= x-dx <= n-1 and dy >=0:
                l = [(x-dx,j) for j in range(m-min(m,1+dy),m)]
            elif x==0 and y == 0 and dx <= 0 and dy <= 0:
                l = [(i,j) for i in range(min(n,1-dx)) for j in range(min(m,1-dy))]
            elif x==n-1 and y == m-1 and dx >= 0 and dy >=0:
                l = [(i,j) for i in range(n-min(n,1+dx),n) for j in range(m-min(m,1+dy),m)]
            elif x== 0 and y == m-1 and dx <= 0 and dy >=0:
                l = [(i,j) for i in range(min(n,1-dx)) for j in range(m-min(m,1+dy),m)]
            elif x == n-1 and y == 0 and dx >= 0 and dy <= 0:
                l = [(i,j) for i in range(n-min(n,1+dx),n) for j in range(min(m,1-dy))]
            new_set.update(l)
            dp[(x,y,dx,dy)] = l
        start_set = new_set
        new_set = set()
    return len(start_set)


#print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(	2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))