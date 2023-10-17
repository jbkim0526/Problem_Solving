import sys 
input = sys.stdin.readline 
from collections import deque

r,c,t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(r)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]

air_con = -1
for i in range(r):
    if board[i][0] == -1:
        air_con = i
        break 

loop1,loop2 = [],[]
for i in range(air_con): loop1.append((i,0))
for j in range(c): loop1.append((air_con,j))
for i in range(air_con-1,0,-1): loop1.append((i,c-1))
for j in range(c-1,0,-1): loop1.append((0,j))
for i in range(air_con+1,r-1): loop2.append((i,0))
for j in range(c-1): loop2.append((r-1,j))
for i in range(r-1,air_con+1,-1): loop2.append((i,c-1))
for j in range(c-1,0,-1): loop2.append((air_con+1,j))

def spread(board):
    new_board = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            cur_val = board[i][j]
            if cur_val == 0:
                continue 
            if cur_val == -1:
                new_board[i][j] = -1
                continue
            spread_val = int(cur_val/5)
            spread_count = 0
            for di,dj in directions:
                ni,nj = i+di,j+dj 
                if ni < 0 or ni>r-1 or nj <0 or nj > c-1 or board[ni][nj] == -1:
                    continue 
                spread_count += 1
                new_board[ni][nj] += spread_val
            new_board[i][j] += board[i][j] - spread_val*spread_count
    return new_board

def refresh(board):
    rotated_loop1, rotated_loop2 = deque(),deque()
    for i,j in loop1: rotated_loop1.append(board[i][j])
    for i,j in loop2: rotated_loop2.append(board[i][j])
    rotated_loop1.rotate(1)
    rotated_loop2.rotate(-1)
    for index,(i,j) in enumerate(loop1):
        if board[i][j] == -1:
            continue
        if rotated_loop1[index] == -1:
            board[i][j] = 0
            continue
        board[i][j] = rotated_loop1[index]
    
    for index,(i,j) in enumerate(loop2):
        if board[i][j] == -1:
            continue
        if rotated_loop2[index] == -1:
            board[i][j] = 0
            continue
        board[i][j] = rotated_loop2[index]

for _ in range(t):
    board = spread(board)
    refresh(board)
    
ans = sum([sum(board[i]) for i in range(r)])
print(ans+2)