def getij(board, s):
    starti = -1
    startj = -1
    for i in range(len(board)):
        if s in board[i]:
            starti = i 
    startj = board[starti].index(s)
    return starti, startj


def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    score = [[0 for _ in range(M)] for _ in range(N)]

    l = []

    si, sj = getij(board,"R")
    di, dj = getij(board,"G")
    l.append((si,sj))

    while len(l) > 0:
        curi,curj = l.pop(0)
        d = score[curi][curj]

        if board[curi][curj] == "G":
            answer = d
            break

        i = curi
        while i > 0 and board[i-1][curj] != "D":
            i -= 1
        if score[i][curj] == 0 or score[i][curj] > d+1:
            score[i][curj] = d+1
            l.append((i,curj))

        # going down
        i = curi
        while i < N-1 and board[i+1][curj] != "D":
            i += 1
        if score[i][curj] == 0 or score[i][curj] > d+1:
            score[i][curj] = d+1
            l.append((i,curj))

        # going left
        j = curj
        while j > 0 and board[curi][j-1] != "D":
            j -= 1
        if score[curi][j] == 0 or score[curi][j] > d+1:
            score[curi][j] = d+1
            l.append((curi,j))
        
        # going right
        j = curj
        while j < M-1 and board[curi][j+1] != "D":
            j += 1
        if score[curi][j] == 0 or score[curi][j] > d+1:
            score[curi][j] = d+1
            l.append((curi,j))

    if score[di][dj] == 0:
        answer = -1

    return answer

print(solution([".D.R", "....", ".G..", "...D"]))