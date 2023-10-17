from collections import deque
n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
l_list = list(map(int, input().split()))
directions = [(0,1),(1,0),(-1,0),(0,-1)]

def is_out(ni,nj):
    return ni < 0 or ni > 2**n-1 or nj<0 or nj>2**n-1
def is_adjacent(i,j):
    res = 0
    for di,dj in directions:
        ni,nj = i+di,j+dj
        if is_out(ni,nj) or board[ni][nj] == 0:
            continue
        res += 1
    return res >= 3

def rotate_board(l):
    if l == 0:
        return
    r = 2**(n-l)
    b = 2**l
    for i in range(r):
        for j in range(r):
            si,sj = i*b,j*b
            temp = [[None for _ in range(b)] for _ in range(b)]
            for di in range(b):
                for dj in range(b):
                    temp[dj][b-1-di] = board[si+di][sj+dj]
            for di in range(b):
                for dj in range(b):
                    board[si+di][sj+dj] = temp[di][dj]

for l in l_list:
    rotate_board(l)

    melt_list = []

    for i in range(2**n):
        for j in range(2**n):
            if board[i][j] ==0 or is_adjacent(i,j):
                continue
            melt_list.append((i,j))

    for i,j in melt_list:
        board[i][j] -= 1



print(sum([sum(board[i]) for i in range(2**n)]))
visited = [[0 for _ in range(2**n)] for _ in range(2**n)]
max_count = -1
for i in range(2**n):
    for j in range(2**n):
        if visited[i][j] or board[i][j] == 0:
            continue
        d = deque([(i,j)])
        visited[i][j] = 1
        cur_count = 1
        while d:
            ci,cj = d.popleft()
            for di,dj in directions:
                ni,nj = ci+di,cj+dj
                if is_out(ni,nj) or visited[ni][nj] or board[ni][nj] == 0:
                    continue
                cur_count += 1
                visited[ni][nj] = 1
                d.append((ni,nj))
        max_count = max(max_count,cur_count)

print(max_count if max_count > 1 else 0)






