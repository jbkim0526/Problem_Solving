from copy import deepcopy

def solution(board, aloc, bloc):
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    row_len,col_len = len(board), len(board[0])
    locations = [tuple(aloc),tuple(bloc)]

    def track(board, locations, turn, depths, win):
        x,y = locations[turn]
        res = -1 
        next_moves = []
        answers = []

        if turn == 0:
            res = 100 if win == 0 else 0
        else:
            res = 0 if win == 0 else 100
        if board[x][y] == 0:
            return depths if win != turn else -1

        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<=row_len-1 and 0<=ny<=col_len-1 and board[nx][ny] == 1:
                next_moves.append((nx,ny))
                
        if len(next_moves) == 0:
            return depths if win != turn else -1

        for nx,ny in next_moves:
            new_board = deepcopy(board)
            new_board[x][y] = 0
            new_locations = locations.copy()
            new_locations[turn] = (nx,ny)
            ans = track(new_board, new_locations, 1 if turn == 0 else 0 , depths+1, win)
            if ans == -1:
                answers.append(-1)
                continue
            answers.append(ans)
        if all(ans == -1 for ans in answers):
            return -1
        if turn == 0:
            res = min(answers, key=lambda x: x if x > 0 else 100) if win == 0 else max(answers)
        else:
            res = max(answers) if win == 0 else min(answers, key=lambda x: x if x > 0 else 100)
        return res
    return min(track(board,locations,0,0,0),track(board,locations,0,0,1),key = lambda x: x if x >= 0 else 100)

print(solution(	[[1, 1, 1, 1, 1]],[0, 0],[0, 4]))


