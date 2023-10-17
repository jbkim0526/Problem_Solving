from math import inf 

def solution(board):
    board_len = len(board)
    score = [[[inf,inf,inf,inf] for _ in range(board_len)] for _ in range(board_len)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    l = [(0,0)]
    score[0][0][0] = 0
    score[0][0][1] = 0

    while len(l) > 0:
        curi,curj = l.pop(0)
        for cur_dir in range(4):
            cur_score = score[curi][curj][cur_dir]
            if cur_score== inf:
                continue 
            for i in range(4):
                if cur_dir == (i+2)%4 :
                    continue 
                di, dj = directions[i]
                ni, nj = curi+di,curj+dj
                if ni<0 or ni>board_len-1 or nj<0 or nj>board_len-1 or board[ni][nj]:
                    continue 
                
                new_score = cur_score + (100 if i == cur_dir else 600) 
                if score[ni][nj][i] > new_score:
                    score[ni][nj][i] = new_score 
                    if (ni,nj) not in l:
                        l.append((ni,nj))

    return min(score[board_len-1][board_len-1])


print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))