import sys
from collections import defaultdict,deque
input = sys.stdin.readline 

n,m,k = map(int, input().split())
reward = [list(map(int, input().split()))for _ in range(n)]
board =[[5 for _ in range(n)] for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

tree_inputs = []
for _ in range(m):
    x,y,life = map(int, input().split())
    tree_inputs.append((x-1,y-1,life))
tree_inputs.sort(key = lambda x: x[2])
for i,j,life in tree_inputs:
    trees[i][j].append(life)

next_positions = defaultdict(list)
for i in range(n):
    for j in range(n):
        for di,dj in directions:
            ni,nj = i+di,j+dj 
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                continue
            next_positions[(i,j)].append((ni,nj))

for _ in range(k):
    dead_trees = []
    # spring
    for i in range(n):
        for j in range(n):
            d = trees[i][j]
            new_d = deque()
            while len(d) > 0:
                life = d.popleft()
                if board[i][j] < life:
                    dead_trees.append((i,j,life))
                else:
                    new_d.append(life+1)
                    board[i][j] -= life
            trees[i][j] = new_d

    # summer
    for i,j,life in dead_trees:
        board[i][j] += int(life/2)

    # autumn 
    for i in range(n):
        for j in range(n):
            for life in trees[i][j]:
                if life % 5 != 0:
                    continue
                for ni,nj in next_positions[(i,j)]:
                    trees[ni][nj].appendleft(1)
    # winter
    for i in range(n):
        for j in range(n):
            board[i][j] += reward[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)