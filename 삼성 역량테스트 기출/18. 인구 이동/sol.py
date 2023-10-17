import sys 
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]

end_count=  n*n
ans = 0
# 연합의 개수가 동일하면?

while True:
    unions = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            p = deque([(i,j)])
            union = set()
            while len(p) > 0:
                curi,curj = p.popleft()
                visited[curi][curj] = True 
                union.add((curi,curj))
                cur_pop = board[curi][curj]

                for di,dj in directions:
                    ni,nj = curi+di, curj+dj
                    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                        continue
                    if visited[ni][nj]:
                        continue 
                    if l <= abs(cur_pop-board[ni][nj]) <= r:
                        p.append((ni,nj))
                    
            unions.append(union)

    if len(unions) == end_count:
        break

    for union in unions:
        if len(union) == 1:
            continue
        total_pop = sum([board[i][j] for i,j in union])
        new_pop = int(total_pop/len(union))
        for i,j in union:
            board[i][j] = new_pop

    ans += 1

print(ans)