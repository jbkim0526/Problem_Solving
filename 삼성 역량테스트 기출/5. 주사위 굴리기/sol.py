import sys 

input = sys.stdin.readline

n,m,i,j,count = map(int, input().split())
board = [list(map(int,input().split())) for i in range(n)]
commands = list(map(int,input().split()))


directions = [(0,1),(0,-1),(-1,0),(1,0)]

dice = [[0 for _ in range(3)] for _ in range(4)]

def movedice(d):
    global i,j
    di,dj = directions[d]
    ni,nj = i+di,j+dj 

    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1:
        return
    i,j = ni,nj
    v = board[i][j]
    
    # 다이스를 일단 굴려
    if d == 0 :
        t = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = t 
    
    elif d == 1 :
        t = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = t

    elif d == 2:
        t = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = t 
    else:
        t = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = t 
        

    if v == 0:
        board[i][j] = dice[3][1]
    else:
        dice[3][1] = v 
        board[i][j] = 0
        
    print(dice[1][1])

for c in commands:
    movedice(c-1)
