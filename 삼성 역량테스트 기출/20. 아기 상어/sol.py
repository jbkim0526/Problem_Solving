import sys 
input = sys.stdin.readline 
from collections import deque

n = int(input()[:-1])

board = [list(map(int,input().split())) for _ in range(n)]
directions = [(-1,0),(0,-1),(0,1),(1,0)]
shark = None
fishes = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 0: continue
        elif board[i][j] == 9: 
            shark = (i,j,2,0)
            board[i][j] = 0
        else: fishes.append((i,j,board[i][j]))

fishes.sort(key = lambda x: -x[2])

ans = 0

while True:

    si,sj,slife,sfood = shark
    # 먹을 수 있는 물고기 x
    if len(fishes) == 0 or fishes[-1][2] >= slife:
        break

    for i,j,fish_life in fishes:
        


    


print(ans)
        