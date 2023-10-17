def solution(rows, columns, queries):
    answer = []
    d = [[columns*j+c+1 for c in range(columns)] for j in range(rows)]
    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        temp = d[x2][y2]
        m = temp 
        for i in reversed(range(x1,x2)):
            d[i+1][y2] = d[i][y2] 
            m = min(m, d[i][y2])
        for i in reversed(range(y1,y2)):
            d[x1][i+1] = d[x1][i] 
            m = min(m, d[x1][i])
        for i in range(x1,x2):
            d[i][y1] = d[i+1][y1] 
            m = min(m, d[i+1][y1])
        for i in range(y1,y2-1):
            d[x2][i] = d[x2][i+1] 
            m = min(m, d[x2][i+1])
        d[x2][y2-1] = temp
        answer.append(m)
    return answer

print(solution(6	,6	,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))