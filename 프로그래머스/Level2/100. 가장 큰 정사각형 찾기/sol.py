def solution(board):
    answer = 0
    m,n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                if board[i][j] == 1:
                    answer = max(answer,1) 
                continue 
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                if board[i][j] > answer:
                    answer = board[i][j]
    return answer*answer



#print(solution([[1,1],[0,0],[1,0],[0,1]]))
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
