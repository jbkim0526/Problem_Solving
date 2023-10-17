import pdb
import sys 
input = sys.stdin.readline 
from collections import deque

n,m,t = map(int,input().split())

plate = [None] + [deque(map(int,input().split())) for _ in range(n)]
rotates = [list(map(int,input().split())) for _ in range(t)]
spins = [1,-1]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
total_sum = sum([sum(plate[i]) for i in range(1,n+1)])
total_count = n*m

for x,d,k in rotates:
    
    # x배수의 원판 k만큼 회전
    spin = spins[d]
    for i in range(x,n+1,x):
        plate[i].rotate(k*spin)
   
    # DFS로 인전한 것들 찾기
    visited = [[False for _ in range(m)] for _ in range(n+1)]
    exist = False


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
                    # 처리를 여기서 하고 append
                    adjacent.add((ni,nj))
                    visited[ni][nj] = True 
                    q.append((ni,nj))

            if len(adjacent) > 1:
                for i,j in adjacent:
                    total_sum -= plate[i][j]
                    total_count -= 1
                    plate[i][j] = None 
                    exist = True
            
    if not exist:
        if total_count == 0:
            break
        avg = total_sum/total_count
        for i in range(1,n+1):
            for j in range(m):
                if not plate[i][j]:
                    continue 
                if plate[i][j] < avg:
                    total_sum += 1
                    plate[i][j] += 1
                elif plate[i][j] > avg:
                    plate[i][j] -= 1
                    total_sum -= 1
ans = 0 
for i in range(1,n+1):
    for j in range(m):
        if not plate[i][j]:
            continue 
        else:
            ans += plate[i][j]
print(ans)
    


                

