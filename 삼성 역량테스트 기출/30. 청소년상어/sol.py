from copy import deepcopy

board = [[None for _ in range(4)] for _ in range(4)]
directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
fishes = [None]*(17)

for i in range(4):
    input_line = list(map(int,input().split()))
    for j in range(4):
        board[i][j] = (input_line[2*j],input_line[2*j+1]-1)
        fishes[input_line[2*j]] = (i,j)

# 초기 상어 (0,0)
f,d = board[0][0]
fishes[f] = None
board[0][0] = (0,d) # shark는 번호가 0
fishes[0] = (0,0)
ans = f
def out_of_range(i,j):
    return i < 0 or i > 3 or j < 0 or j > 3

def swap_fishes(fishes,f1,f2):
    temp = fishes[f1]
    fishes[f1] = fishes[f2]
    fishes[f2] = temp

def moveFish(board,fishes):
    for fish_num in range(1,17):
        if not fishes[fish_num]:
            continue
        ci,cj = fishes[fish_num]
        _,d = board[ci][cj]
        for _ in range(8):
            di,dj = directions[d]
            ni,nj = ci+di,cj+dj
            # 범위 밖 : 회전
            if out_of_range(ni,nj):
                d = (d+1) % 8
                continue
            # 빈 칸: 이동
            if board[ni][nj] == None:
                board[ni][nj] = (fish_num,d)
                board[ci][cj] = None
                fishes[fish_num] = (ni,nj)
                break

            # 상어 : 회전
            if board[ni][nj][0] == 0:
                d = (d+1) % 8
                continue
            # 물고기가 있으면 자리를 바꿈
            else:
                swap_fishes(fishes,fish_num, board[ni][nj][0])
                board[ci][cj] = board[ni][nj]
                board[ni][nj] = (fish_num,d)
                break

def track(board,fishes):

    moveFish(board,fishes)

    shark_candidates = []
    ci,cj = fishes[0]
    di,dj = directions[board[ci][cj][1]]
    ni,nj = ci+di,cj+dj

    while 0<=ni<=3 and 0<=nj<=3:
        if not board[ni][nj]:
            ni += di;nj += dj
            continue
        shark_candidates.append((ni,nj))
        ni += di ; nj += dj

    if not shark_candidates:
        return 0

    res = []
    # 이동할 수 있으면 -> 먹고 이동
    for ni,nj in shark_candidates:
        new_board = deepcopy(board)
        new_fishes = fishes.copy()
        # 먹힐 물고기의 f,d
        f,d = board[ni][nj]
        new_board[ni][nj] = (0,d)
        new_board[ci][cj] = None
        new_fishes[f] = None
        new_fishes[0] = (ni,nj)
        res.append(f + track(new_board,new_fishes))
    return max(res)

ans += track(board,fishes)
print(ans)