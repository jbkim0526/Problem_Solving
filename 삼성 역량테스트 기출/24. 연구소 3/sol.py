import sys 
from math import inf
from copy import deepcopy
input = sys.stdin.readline 
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in  range(n)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
empty_spaces = 0
start_virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            start_virus.append((i,j))
        if board[i][j] == 0:
            empty_spaces += 1
len_virus = len(start_virus)


def spread_time(s_virus, board):

    # 비활성 애들은 3으로 둠
    for i,j in start_virus:
        if (i,j) in s_virus:
            continue
        board[i][j] = 3

    edge_virus = s_virus
    spread_spaces = 0
    time = 0
    while spread_spaces < empty_spaces:
        new_edge_virus = set()
        for i,j in edge_virus:
            for di,dj in directions:
                ni,nj = i+di,j+dj 
                if ni < 0 or ni > n-1 or nj < 0 or nj > n-1 or board[ni][nj] in [1,2]:
                    continue
                if board[ni][nj] == 0:
                    spread_spaces += 1
                    board[ni][nj] = 2
                else:
                    board[ni][nj] = 2
                new_edge_virus.add((ni,nj))
    
        if len(new_edge_virus) == 0:
            break

        for i,j in new_edge_virus:
            board[i][j] = 2
        time += 1
        edge_virus = new_edge_virus

    if spread_spaces < empty_spaces:
        return inf
    return time


def track(virus, start):
    ans = inf
    if len(virus) == m:
        return spread_time(virus.copy(),deepcopy(board))
    for i in range(start,len_virus):
        virus.append(start_virus[i])
        ans = min(track(virus,i+1),ans)
        virus.pop()
    return ans

res = track([],0)
print(res if res != inf else -1)


