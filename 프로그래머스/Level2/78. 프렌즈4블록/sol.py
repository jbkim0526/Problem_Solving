
def solution(m, n, board):
    answer = 0

    l = []
    for j in range(n):
        t = []
        for i in range(m):
            t.append(board[i][j])
        l.append(t)

    while True:
        toRemove = set()
        for i in range(n-1):
            for j in range(m-1):
                if l[i][j] == l[i+1][j] == l[i][j+1] == l[i+1][j+1] and l[i][j]:
                    toRemove.add((i,j)); toRemove.add((i,j+1))
                    toRemove.add((i+1,j)); toRemove.add((i+1,j+1))
        remove_len = len(toRemove)
        if remove_len == 0:
            break
        for i,j in toRemove:
            l[i][j] = ""
        answer += remove_len
        for i in range(n):
            l[i].sort(key = lambda x: len(x))

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))