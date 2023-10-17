
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ans = 0

def outofBounds(ni,nj):
    return ni < 0 or ni > n - 1 or nj < 0 or nj > n - 1
def update_board(i,j,d):
    global ans
    di,dj = directions[d]
    li,lj = directions[(d+1)%4]
    ri,rj = directions[(d-1)%4]
    sand = board[i][j]
    nears = [(2,0,0,0.05),(1,0,1,0.1),(1,1,0,0.1),(0,1,0,0.07),(0,0,1,0.07),(0,2,0,0.02),(0,0,2,0.02),(-1,1,0,0.01),(-1,0,1,0.01)]

    for front,left,right,rate in nears:
        ni = i+front*di+left*li+right*ri
        nj = j+front*dj+left*lj+right*rj
        n_sand = int(board[i][j]*rate)
        # 밖에 나가는 모래
        if outofBounds(ni,nj):
            ans += n_sand
        # 내부에 있는 모래
        else:
            board[ni][nj] += n_sand
        sand -= n_sand
    # alpha칸 고려하기
    ai,aj = i+di,j+dj
    if outofBounds(ai,aj):
        ans += sand
    else:
        board[ai][aj] += sand
    board[i][j] = 0

def main():
    i, j = n // 2, n // 2
    d, l, update = 0, 1, False
    l = 1
    while True:
        di,dj = directions[d]
        for _ in range(l):
            i += di ; j += dj
            update_board(i,j,d)
            if i == 0 and j ==0:
                return
        d = (d+1)%4
        if update:
            l += 1
            update = False
        else:
            update = True

main()

print(ans)


