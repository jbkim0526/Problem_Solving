import sys 
from collections import deque
input = sys.stdin.readline


n = int(input()[:-1])

curves = [list(map(int,input().split())) for _ in range(n)]
directions = [(1,1),(-1,0),(0,-1),(1,0)]

lines = set()

for x,y,d,g  in curves:
    shape = deque([d])
    for _ in range(g):
        for i in range(len(shape)-1,-1,-1):
            shape.append((shape[i]+1) % 4)
    bx,by = x,y
    for s in shape:
        dx,dy = directions[s]
        cx,cy = bx+dx,by+dy
        lines.add((bx,by,cx,cy))
        lines.add((cx,cy,bx,by))
        bx,by = cx,cy 

print(lines)

def isSquare(i,j):
    if (i,j,i+1,j) not in lines:
        return False
    if (i,j,i,j+1) not in lines:
        return False
    if (i,j+1,i+1,j+1) not in lines:
        return False
    if (i+1,j,i+1,j+1) not in lines:
        return False
    return True

ans = 0
for i in range(100):
    for j in range(100):
        if isSquare(i,j):
            ans += 1

print(ans)