# 시간초과는 해결
def solution(clockHands):
    answer = 0
    n = len(clockHands)
    directions = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]
    grid = [[(4 - clockHands[i][j]) % 4 for j in range(n)] for i in range(n)]
    total = sum([sum(grid[i]) for i in range(n)])
    score = [[0 for _ in range(n)] for _ in range(n)]

    def getScore(i,j):
        score = 0
        for di,dj in directions:
            if 0<=i+di<=n-1 and 0<=j+dj<=n-1: 
                if grid[i+di][j+dj] == 0: 
                    score -= 3
                else:
                    score += 1
        return score

    for i in range(n):
        for j in range(n):
            score[i][j] = getScore(i, j)
    print(score)
    while total > 0:
        maxscore = 0 ; maxi, maxj = -1,-1
        for i in range(n):
            for j in range(n):
                s = score[i][j]
                if s > maxscore:
                    maxscore = s
                    maxi,maxj = i,j
        for di,dj in directions:
            ni = maxi+di ; nj = maxj+dj
            if 0<=ni<=n-1 and 0<=nj<=n-1 and grid[ni][nj] == 1:
                for di,dj in directions:
                    if 0<=ni+di<=n-1 and 0<=nj+dj<=n-1:
                        score[ni+di][nj+dj] =  (score[ni+di][nj+dj]-1) % 4
        print(maxscore)
        print(score)
        total -= maxscore
        answer += 1     
    return answer

print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))
#print(solution([[0,3,3,0,0,0,0,0],[3,2,2,3,0,0,0,0],[0,3,2,0,0,0,0,0],[0,3,3,3,0,0,0,0],[0,0,3,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]))