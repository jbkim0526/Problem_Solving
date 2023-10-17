from collections import defaultdict

def solution(clockHands):
    answer = 0
    n = len(clockHands)
    grid_directions = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]
    score_directions = [(0,0),(-1,0),(-2,0),(-1,-1),(0,1),(1,1),(0,2),(1,0),(2,0),(1,-1),(0,-1),(0,-2),(-1,1)]
    update_grid_dict = defaultdict(list)
    update_score_dict = defaultdict(list)
    grid = [[(4 - clockHands[i][j]) % 4 for j in range(n)] for i in range(n)]
    score = [[0 for _ in range(n)] for _ in range(n)]
    total = sum([sum(grid[i]) for i in range(n)])

    def getScore(i,j):
        score = 0
        for di,dj in grid_directions:
            if 0<=i+di<=n-1 and 0<=j+dj<=n-1: 
                if grid[i+di][j+dj] != 0: 
                    score += 1
                else:
                    score -= 1
        return score

    for i in range(n):
        for j in range(n):
            score[i][j] = getScore(i, j)
            for di, dj in grid_directions:
                if 0<=i+di<=n-1 and 0<=j+dj<=n-1: 
                    update_grid_dict[(i,j)].append((i+di,j+dj))
            for di, dj in score_directions:
                if 0<=i+di<=n-1 and 0<=j+dj<=n-1: 
                    update_score_dict[(i,j)].append((i+di,j+dj))

    while total > 0:
        maxscore = -100 ; maxi, maxj = -1,-1
       
        for i in range(n):
            for j in range(n):
                s = score[i][j]
                if s > maxscore:
                    maxscore = s
                    maxi,maxj = i,j

        for i,j in update_grid_dict[(maxi,maxj)]:
            grid[i][j] = (grid[i][j] - 1) % 4
        for i,j in update_score_dict[(maxi,maxj)]:
            score[i][j] = getScore(i, j)      
        total -= maxscore
        answer += 1  

    return answer

#print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))
print(solution([[0,0,0,0],[0,0,0,0],[1,0,3,0],[1,0,3,3]]))
#print(solution([[0,3,3,0,0,0,0,0],[3,2,2,3,0,0,0,0],[0,3,2,0,0,0,0,0],[0,3,3,3,0,0,0,0],[0,0,3,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]))