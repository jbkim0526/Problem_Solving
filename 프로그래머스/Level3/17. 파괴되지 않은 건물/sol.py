from collections import defaultdict

def solution(board, skill):
    answer = 0
    m = len(board)
    n = len(board[0])
    ranges = defaultdict(int)

    for t,r1,c1,r2,c2,degree in skill:
        d = degree if t == 2 else -degree 
        ranges[(r1,c1,r2,c2)] += d 
    
    for (r1,c1,r2,c2), d in ranges.items():
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                board[i][j] += d 
    
    for i in range(m):
        for j in range(n):
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))