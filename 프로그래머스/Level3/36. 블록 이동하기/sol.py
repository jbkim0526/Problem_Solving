from math import inf

def solution(board):
    answer = 0

    n = len(board)
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    spins = [(1,0),(0,1)]
    score = [[[inf,inf] for _ in range(n)] for _ in range(n)]

    l = [((0,0,1))]
    score[0][0][1] = 0

    while len(l) > 0:
        x1,y1,shape = l.pop(0)
        next_coords = []
        if shape == 0:
            x2= x1+1 
            if y1+1 <= n-1 and board[x1][y1+1] == 0 and board[x2][y1+1] == 0:
                next_coords.append((x1,y1+1,0))
                next_coords.append((x1,y1,1))
                next_coords.append((x2,y1,1))
            if y1-1 >= 0 and board[x1][y1-1] == 0 and board[x2][y1-1] == 0:
                next_coords.append((x1,y1-1,0))
                next_coords.append((x1,y1-1,1))
                next_coords.append((x2,y1-1,1))
            if x1-1 >= 0 and board[x1-1][y1] == 0:
                next_coords.append((x1-1,y1,0))
            if x2+1 <= n-1 and board[x2+1][y1] == 0:
                next_coords.append((x2,y1,0))

        elif shape == 1:
            y2 = y1+1
            if x1+1 <= n-1 and board[x1+1][y1] == 0 and board[x1+1][y2] == 0:
                next_coords.append((x1+1,y1,1))
                next_coords.append((x1,y1,0))
                next_coords.append((x1,y2,0))
            if x1-1 >= 0 and board[x1-1][y1] == 0 and board[x1-1][y2] == 0:
                next_coords.append((x1-1,y1,1))
                next_coords.append((x1-1,y1,0))
                next_coords.append((x1-1,y2,0))
            if y1-1>=0 and board[x1][y1-1] == 0:
                next_coords.append((x1,y1-1,1))
            if y2+1<=n-1 and board[x1][y2+1] == 0:
                next_coords.append((x1,y2,1))

        new_score = score[x1][y1][shape] + 1
        for nx,ny,s in next_coords:
            if new_score < score[nx][ny][s]:
                score[nx][ny][s] = new_score 
                l.append((nx,ny,s))

    return  min(score[n-1][n-2][1], score[n-2][n-1][0])


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))