def solution(clockHands):
    answer = 0

    n = len(clockHands)
    directions = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]
    grid = [[(4 - clockHands[i][j]) % 4 for j in range(n)] for i in range(n)]
    score = [[0 for _ in range(n)] for _ in range(n)]
    total = sum([sum(grid[i]) for i in range(n)])


    def getScore(i,j):
        score = 0
        for di,dj in directions:
            if 0<=i+di<=n-1 and 0<=j+dj<=n-1:
                adj_node = grid[i+di][j+dj]
                if adj_node == 0: 
                    score -= 3
                else:
                    score += adj_node
        return score

    # for i in range(n):
    #     for j in range(n):
    #         s,z = getScore(i, j)
    #         score[i][j] = s 
  


    while total > 0:
        score_list = []
        for i in range(n):
            for j in range(n):
                s,z = getScore(i, j)
                score_list.append((s,z,i,j))
        score_list.sort(key= lambda x: (x[0],-x[1]))
        maxi, maxj = score_list[-1][2],score_list[-1][3]
        for di,dj in directions:
            if 0<=maxi+di<=n-1 and 0<=maxj+dj<=n-1:
                if grid[maxi+di][maxj+dj] == 0:
                    grid[maxi+di][maxj+dj] = 3
                    total += 3
                else:
                    grid[maxi+di][maxj+dj] -= 1
                    total -= 1
        answer += 1
    return answer

print(solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]))