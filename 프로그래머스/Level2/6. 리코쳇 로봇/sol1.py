from math import inf 
minlen = inf

def track(board, path,N,M):
    global minlen
    curi, curj = path[-1]
    print(path)
    if board[curi][curj] == "G":
        if minlen > len(path):
            minlen = len(path)
            return
    if len(path) > minlen:
        return
    # going up
    i = curi
    while i > 0 and board[i-1][curj] != "D":
        i -= 1
    if (i,curj) in path:
        pass
    else:
        temp = path.copy()
        temp.append((i,curj))
        track(board,temp,N,M)

    # going down
    i = curi
    while i < N-1 and board[i+1][curj] != "D":
        i += 1
    if (i,curj) in path:
        pass
    else:
        temp = path.copy()
        temp.append((i,curj))
        track(board,temp,N,M)

    # going left
    j = curj
    while j > 0 and board[curi][j-1] != "D":
        j -= 1
    if (curi,j) in path:
        pass
    else:
        temp = path.copy()
        temp.append((curi,j))
        track(board,temp,N,M)
    
    # going right
    j = curj
    while j < M-1 and board[curi][j+1] != "D":
        j += 1
    if (curi,j) in path:
        pass
    else:
        temp =path.copy()
        temp.append((curi,j))
        track(board,temp,N,M)
        

def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    starti = -1
    startj = -1
    for i in range(N):
        if "R" in board[i]:
            starti = i 
    startj = board[starti].index("R")
    track(board, [(starti, startj)],N,M)
 
    if minlen == inf:
        answer = -1
    else:
        answer = minlen -1
    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))