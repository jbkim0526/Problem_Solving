n,m,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
players = [list(map(int,input().split()))+[0] for _ in range(m)]
guns = [[[] for _ in range(n+1)] for _ in range(n+1)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
scores = [0 for _ in range(m)]

# x,y,d,s

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue
        guns[i+1][j+1].append(board[i][j])

def is_out(i,j):
    return i<1 or i>n or j<1 or j>n

def fight_result(i,j):
    xi,yi,di,si,gi = players[i]
    xj,yj,dj,sj,gj = players[j]
    score_i = si+gi
    score_j = sj+gj
    score = abs(score_i-score_j)
    if score_i > score_j:
        return i,j,score
    elif score_i < score_j:
        return j,i,score
    else:
        if si > sj:
            return i,j,score
        else:
            return j,i,score

# i,j에 본인외에 플레이어
def is_player(x,y,i):
    for p,(xo,yo,_,_,_) in enumerate(players):
        if x == xo and y == yo and p != i:
            return p
    return None

def move_loser(i):
    x,y,d,s,g = players[i]
    # 총을 먼저 내려놔야함.
    if g:
        guns[x][y].append(g)
        g =0
    # 다음 이동할 칸 결정
    nx,ny = -1,-1
    while True:
        dx,dy = directions[d]
        nx,ny = x+dx,y+dy
        if is_out(nx,ny) or is_player(nx,ny,i) is not None:
            d = (d+1)%4
            continue
        break
    players[i] = [nx,ny,d,s,g]
    get_best_gun(i)

# 현재 위치에서 제일 좋은 총 획득
def get_best_gun(i):
    x,y,d,s,g = players[i]
    if g:
        guns[x][y].append(g)
    if guns[x][y]:
        g = max(guns[x][y])
        guns[x][y].remove(g)
    players[i] = [x,y,d,s,g]
def move_player(i):
    x,y,d,s,g = players[i]
    dx,dy = directions[d]
    nx,ny = x+dx,y+dy
    if is_out(nx,ny):
        d = (d+2) % 4
        dx,dy = directions[d]
        nx,ny = x+dx, y+dy
    # 일단 이동을 먼저함
    players[i] = [nx,ny,d,s,g]
    # 이동한 칸에 나말고 있는지 확인
    j = is_player(nx,ny,i)
    if j != None:
        wi,li,score = fight_result(i,j)
        move_loser(li)
        get_best_gun(wi)
        scores[wi] += score
    else:
        get_best_gun(i)

for _ in range(k):
    for p in range(m):
        move_player(p)

print(*scores)
