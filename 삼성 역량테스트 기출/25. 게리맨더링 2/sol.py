import sys 
input = sys.stdin.readline 
from math import inf

n = int(input()[:-1])
board = [[0]*(n+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
total_sum = sum([sum(row) for row in board])
def getmindiff(x,y,d1,d2):

    area = [0,0,0,0,0]
    area5_boundary = set()

    area5_boundary.add((x,y))
    for i in range(1,d1+1):
        area5_boundary.add((x+i,y-i))
    for i in range(1,d2+1):
        area5_boundary.add((x+i,y+i))
    for i in range(1,d2+1):
        area5_boundary.add((x+d1+i,y-d1+i))
    for i in range(1,d1+1):
        area5_boundary.add((x+d2+i,y+d2-i))

    for r in range(1,x+d1):
        for c in range(1,y+1):
            if (r,c) in area5_boundary:
                break 
            area[0] += board[r][c]

    for r in range(1,x+d2+1):
        for c in range(n,y,-1):
            if (r,c) in area5_boundary:
                break 
            area[1] += board[r][c]

    for r in range(x+d1,n+1):
            for c in range(1,y-d1+d2):
                if (r,c) in area5_boundary:
                    break 
                area[2] += board[r][c]

    for r in range(x+d2+1,n+1):
            for c in range(n,y-d1+d2-1,-1):
                if (r,c) in area5_boundary:
                    break 
                area[3] += board[r][c]
    
    area[4] = total_sum - sum(area)
    return max(area)-min(area)

ans = inf
for x in range(1,n+1):
    for y in range(1,n+1):
        # 기준점 (x,y)
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if x+d1+d2 <= n and 1 <= y-d1 and y+d2 <= n:
                    # 가능한 d1,d2들에 대해서
                    ans = min(ans,getmindiff(x, y, d1, d2)) 

print(ans)