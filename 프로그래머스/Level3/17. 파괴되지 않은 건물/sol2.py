def solution(board, skill):
    answer = 0
    row_len = len(board)
    col_len = len(board[0])
    acc_board = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]

    for t,r1,c1,r2,c2,degree in skill:
        d = degree if t == 2 else -degree 
        acc_board[r1][c1] += d 
        acc_board[r1][c2+1] -= d 
        acc_board[r2+1][c1] -= d 
        acc_board[r2+1][c2+1] += d
    
    for i in range(row_len):
        for j in range(col_len):
            acc_board[i][j+1] += acc_board[i][j]

    for j in range(col_len):
        for i in range(row_len):
            acc_board[i+1][j] += acc_board[i][j]

    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] + acc_board[i][j] > 0:
                answer += 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))