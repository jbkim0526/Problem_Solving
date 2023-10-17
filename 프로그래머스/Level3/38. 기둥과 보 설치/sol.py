

def solution(n, build_frame):
    answer = []
    board  = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    PILLAR = 0 ; BO = 1
    check = [[(0,1),(-1,1)],[(0,-1),(1,0),(-1,0)]]

    def canBuildPillar(x,y):
        if y == n:
            return False
        if y == 0 or board[x][y-1] == 0:
            return True 
        if x >= 1 and board[x-1][y] == 1:
            return True 
        return False 

    def canBuildBo(x,y):
        if x == n:
            return False
        if y == 0:
            return False
        if board[x][y-1] == PILLAR or board[x+1][y-1] == PILLAR:
            return True  
        if x-1 >=0 and x+1 <=n and board[x-1][y] == 1 and board[x+1][y] == 1:
            return True
        return False


    def isValid(x,y,t):
        if t == PILLAR:
            if board[x][y-1] == PILLAR or board[x-1][y] == BO:
                return True 
            return False
        if t == BO:
            if board[x][y-1] == PILLAR or board[x+1][y-1] == PILLAR:
                return True 
            if board[x-1][y] == BO and board[x+1][y] == BO:
                return True 
            return False

    for x,y,a,b in build_frame:

        if b == 1:
            if a == PILLAR:
                if canBuildPillar(x, y):
                    board[x][y] = 0
            else:
                if canBuildBo(x, y):
                    board[x][y] = 1
        else:
            board[x][y] = -1
            valid = True
            for dx,dy in check[a]:
                nx,ny = x+dx,y+dy
                if 0<=nx<=n and 0<=ny<=n and board[nx][ny] != -1:
                    if not isValid(nx, ny, board[nx][ny]):
                        valid = False
                        break      
            if not valid:
                board[x][y] = a

    for x in range(n+1):
        for y in range(n+1):
            if board[x][y] != -1:
                answer.append([x,y,board[x][y]])
                
    return answer


#print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))