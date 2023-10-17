def solution(board, aloc, bloc):
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    row_len,col_len = len(board), len(board[0])

    def track(board, locations, turn):
        x,y = locations[turn]
        can_win = False
        max_count, min_count = 0,1000
        next_moves = []

        if board[x][y] == 0:
            return False, 0

        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<=row_len-1 and 0<=ny<=col_len-1 and board[nx][ny]:
                next_moves.append((nx,ny))

        if len(next_moves) == 0:
            return False, 0

        board[x][y] = 0
        for nx,ny in next_moves:
            locations[turn] = [nx,ny]
            ans = track(board, locations, 1 if turn == 0 else 0)
            if not ans[0]:
                can_win = True
                min_count = min(min_count,ans[1]+1)
            elif not can_win:
                max_count = max(max_count,ans[1]+1)

            locations[turn] = [x,y]

        board[x][y] = 1
        return (True, min_count) if can_win else (False, max_count)

    return track(board,[aloc,bloc],0)[1]

print(solution([[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]], [0, 0], [3, 3]))


