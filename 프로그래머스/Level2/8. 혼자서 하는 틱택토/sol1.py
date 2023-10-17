
def checkWin(board, s):
    win = False 

    for row in board:
        if row[0] == row[1] == row[2] == s:
            win = True 
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == s:
            win = True 
    if board[0][0] == board[1][1] == board[2][2] == s:
        win = True 
    if board[2][0] == board[1][1] == board[0][2] == s:
        win = True
    return win 


def solution(board):
    answer = 1

    o_num = 0
    x_num = 0

    for row in board:
        for elem in row:
            if elem == "O":
                o_num += 1
            elif elem == "X":
                x_num += 1

    if o_num < x_num:
        answer = 0
    elif o_num == x_num:
        if checkWin(board, "O"):
            answer = 0

    elif o_num == x_num + 1:
        if checkWin(board, "X"):
            answer = 0
    else:
        answer = 0

    return answer

print(solution(["...", "...", "..."]))