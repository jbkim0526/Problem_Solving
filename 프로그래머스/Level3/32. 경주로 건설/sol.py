from math import inf 

def solution(board):
    answer = 0

    for row in board :
        print(row)


    board_len = len(board)
    score = [[[inf,[]] for _ in range(board_len)] for _ in range(board_len)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    l = [(0,0)]
    score[0][0][0] = 0
    score[0][0][1] = [0,1]

    while len(l) > 0:
        curi,curj = l.pop(0)
        cur_score, cur_dirs = score[curi][curj]
        for cur_dir in cur_dirs:
            for i in range(4):
                if cur_dir == (i+2)%4 :
                    continue 
                di, dj = directions[i]
                ni, nj = curi+di,curj+dj

                if ni<0 or ni>board_len-1 or nj<0 or nj>board_len-1 or board[ni][nj]:
                    continue 
                
                new_score = cur_score + (100 if i == cur_dir else 600) 
                if score[ni][nj][0] > new_score:
                    score[ni][nj][0] = new_score 
                    score[ni][nj][1] = [i]
                    if (ni,nj) not in l:
                        l.append((ni,nj))
                elif score[ni][nj][0] == new_score:
                    score[ni][nj][1].append(i)
                    if (ni,nj) not in l:
                        l.append((ni,nj))
    for row in score:
        print(row)
    return score[board_len-1][board_len-1][0]


print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))