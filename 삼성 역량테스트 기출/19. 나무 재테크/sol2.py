import sys
from collections import defaultdict
input = sys.stdin.readline 

n,m,k = map(int, input().split())
reward = [list(map(int, input().split()))for _ in range(n)]
board =[[5 for _ in range(n)] for _ in range(n)]
trees = []
directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

next_positions = {}

for i in range(n):
    for j in range(n):
        next_pos = []
        for di,dj in directions:
            ni,nj = i+di,j+dj 
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                continue
            next_pos.append((ni,nj))
        next_positions[(i,j)] = next_pos

for _ in range(m):
    x,y,life = map(int, input().split())
    trees.append((x-1,y-1,life))

for _ in range(k):
    trees.sort(key = lambda x : x[2])
    new_tree = []
    dead_trees = []
    # spring
    for x,y,life in trees:
        if board[x][y] < life:
            dead_trees.append((x,y,life))
        else:
            new_tree.append((x,y,life+1))
            board[x][y] -= life
    trees = new_tree
    # summer
    for x,y,life in dead_trees:
        board[x][y] += int(life/2)
    # autumn 
    for x,y,life in trees:
        if life % 5 != 0:
            continue 
        for ni,nj in next_positions[(x,y)]:
            trees.append((ni,nj,1))
    # winter
    for i in range(n):
        for j in range(n):
            board[i][j] += reward[i][j]

print(len(trees))