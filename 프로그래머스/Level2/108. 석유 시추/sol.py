from collections import deque

def solution(land):

    n,m = len(land), len(land[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    oils = [0 for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] or not land[i][j]:
                continue

            q = deque([(i,j)])
            visited[i][j] = True
            oil_cluster = set([j])
            oil_cluster_count = 1

            while q:
                ci,cj = q.popleft()
                for di,dj in directions:
                    ni,nj = ci+di,cj+dj 
                    # 범위 밖이거나
                    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1:
                        continue 
                    # 이미 조사한 땅 or 석유가 아닌 땅
                    if visited[ni][nj] or not land[ni][nj]:
                        continue 
                    
                    visited[ni][nj] = True 
                    oil_cluster.add(nj)
                    oil_cluster_count += 1
                    q.append((ni,nj))
            
            for rj in oil_cluster:
                oils[rj] += oil_cluster_count
    
    return max(oils)



print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))