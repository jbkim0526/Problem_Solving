def solution(n):
    answer = []

    grid = [[-1 for _ in range(row+1) ] for row in range(n)]
    direction = [(1,0), (0,1), (-1,-1)]
    total = n*(n+1)//2
    i = j = 0
    num = 1
    d = 0

    while num < total+1:
        grid[i][j] = num 
        di, dj = direction[d]
        if i+di > n-1 or j+dj > i or grid[i+di][j+dj] != -1:
            d = (d+1) % 3
            di, dj = direction[d]
        i += di 
        j += dj
        num += 1

    for i in range(n):
        for j in range(i+1):
            answer.append(grid[i][j])

    return answer

print(solution(5))