import sys 
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

directions = ["R","L","U","D"]

def moveboard(board, d):

    if d in ["U","D"]:

        for j in range(n):
            save_i = 0 if d == "U" else n-1
            end_i = n if d == "U" else -1
            i = save_i 
            di = 1  if d == "U" else - 1 
            reg = 0

            while i != end_i:
                if board[i][j] == 0:
                    i += di
                    continue
                if reg == 0:
                    reg = board[i][j]
                    i += di 
                    continue
                if board[i][j] == reg:
                    board[save_i][j] = reg*2
                    reg = 0                         
                else:
                    board[save_i][j] = reg
                    reg = board[i][j]  
                save_i += di          
                i += di

            if reg != 0:
                board[save_i][j] = reg 
                save_i += di

            while save_i != end_i:
                board[save_i][j] = 0
                save_i += di

    if d in ["L","R"]:
        
        for i in range(n):
            save_j = 0 if d == "L" else n-1
            end_j = n if d == "L" else -1
            j = save_j 
            dj = 1  if d == "L" else - 1 
            reg = 0

            while j != end_j:
                if board[i][j] == 0:
                    j += dj
                    continue
                if reg == 0:
                    reg = board[i][j]
                    j += dj
                    continue
                if board[i][j] == reg:
                    board[i][save_j] = reg*2
                    reg = 0                         
                else:
                    board[i][save_j] = reg
                    reg = board[i][j]  
                save_j += dj          
                j += dj

            if reg != 0:
                board[i][save_j] = reg 
                save_j += dj

            while save_j != end_j:
                board[i][save_j] = 0
                save_j += dj



def track(board, depth):
    if depth == 5:
        max_vals = [max(row) for row in board]
        return max(max_vals)
    
    answers = []
    for d in directions:
        cur_board = deepcopy(board)
        moveboard(cur_board, d)
        answers.append(track(cur_board,depth+1))
    
    return max(answers)

print(track(board,0))



