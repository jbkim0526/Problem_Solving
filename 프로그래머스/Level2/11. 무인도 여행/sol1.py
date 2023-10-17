def solution(maps):
    answer = []

    M = len(maps)
    N = len(maps[0])

    score = []

    for row in maps:
        temp = []
        for elem in row:
            temp.append(elem)
        score.append(temp)
    
    
    for i in range(M):
        for j in range(N):
            d = score[i][j]
            if d != 'X':
                l = [(i,j)]
                total = 0
                # do dfs:
                while len(l) > 0:
                    curi, curj = l.pop(0)
                    total += int(score[curi][curj])
                    score[curi][curj] = 'X'
                    # go up 
                    if curi > 0 and score[curi-1][curj] != 'X' and (curi-1,curj) not in l:
                        l.append((curi-1,curj))
                    # go down 
                    if curi < M-1 and score[curi+1][curj] != 'X'and (curi+1,curj) not in l:
                        
                        l.append((curi+1,curj))
                    # go left 
                    if curj > 0 and score[curi][curj-1] != 'X' and (curi,curj-1) not in l:
                        
                        l.append((curi,curj-1))
                    # go right
                    if curj < N-1 and score[curi][curj+1] != 'X'and (curi,curj+1) not in l:
                        l.append((curi,curj+1))

                answer.append(total)
        
    if len(answer) >0:
        answer.sort()
    else:
        answer.append(-1)

    return answer


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))