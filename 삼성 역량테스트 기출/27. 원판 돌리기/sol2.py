import sys 
input = sys.stdin.readline 
from collections import deque

n,m,t = map(int,input().split())

plate = [None] + [deque(map(int,input().split())) for _ in range(n)]
rotates = [list(map(int,input().split())) for _ in range(t)]
spins = [1,-1]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
numbers_count = n*m

for x,d,k in rotates:
    # x배수의 원판 k만큼 회전
    spin = spins[d]
    for i in range(x,n+1,x):
        plate[i].rotate(k*spin)
    
    # DFS로 인전한 것들 찾기
    visited = [[False for _ in range(m)] for _ in range(n+1)]
    adjacent_lists = []
    for i in range(1,n+1):
        for j in range(m):
            if visited[i][j]:
                continue 
            if not plate[i][j]:
                continue
            val = plate[i][j]
            q = deque([(i,j)])
            visited[i][j] = True 
            adjacent = set([(i,j)])
            while len(q) > 0:
                ci,cj = q.popleft()
                for di,dj in directions:
                    ni,nj = ci+di,(cj+dj) % m 
                    if ni < 1 or ni > n:
                        continue
                    if not plate[ni][nj] or visited[ni][nj]:
                        continue 
                    if plate[ni][nj] != val:
                        continue 
                    visited[ni][nj] = True
                    q.append((ni,nj))
                    adjacent.add((ni,nj))
            adjacent_lists.append(adjacent)
    # 인접한 게 없음
    if len(adjacent_lists) == numbers_count:
        add = 0
        count = 0
        for i in range(1,n+1):
            for j in range(m):
                if not plate[i][j]:
                    continue 
                count += 1
                add += plate[i][j]
        if count == 0:
            break
        avg = add/count 
        for i in range(1,n+1):
            for j in range(m):
                if not plate[i][j]:
                    continue 
                if plate[i][j] < avg:
                    plate[i][j] += 1
                elif plate[i][j] > avg:
                    plate[i][j] -= 1
    else:
        for adjacent in adjacent_lists:
            if len(adjacent) == 1:
                continue 
            for i,j in adjacent:
                plate[i][j] = None 
                numbers_count -= 1
      

ans = 0 
for i in range(1,n+1):
    for j in range(m):
        if not plate[i][j]:
            continue 
        else:
            ans += plate[i][j]
print(ans)
    


                

