

n,m,k,c = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

directions = [(0,1),(1,0),(0,-1),(-1,0)]
diagnals = [(1,1),(1,-1),(-1,-1),(-1,1)]

# 어느 좌표표가 어느세대까지 막혔다고 표시.
blocked = [[0 for _ in range(n)] for _ in range(n)]
def is_out(i,j):
    return i < 0 or i > n-1 or j < 0 or j > n-1

def grow_tree():
    # 추가량 기록
    deltas = []
    for i in range(n):
        for j in range(n):
            # 나무가 있는 땅에서
            if board[i][j] <= 0:
                continue
            # 주위 나무개수 조사
            cnt = 0
            for di,dj in directions:
                ni,nj=i+di,j+dj
                # 나무가 아니면 무시
                if is_out(ni,nj) or board[ni][nj] <= 0:
                    continue
                cnt += 1
            deltas.append((i,j,cnt))
    for i,j,delta in deltas:
        board[i][j] += delta
# year 잘 작동하는지 확인
def tree_spread(year):
    deltas = []
    for i in range(n):
        for j in range(n):
            # 나무가 있는 땅에서
            if board[i][j] <= 0:
                continue
            # 번식할 수 있는 주위 칸을 찾음
            l = []
            for di,dj in directions:
                ni,nj=i+di,j+dj
                # 범위 밖, 나무, 벽인 경우
                if is_out(ni,nj) or board[ni][nj] or board[ni][nj] == -1:
                    continue
                # 제초제효과가 남아있으면
                if blocked[ni][nj] >= year:
                    continue
                l.append((ni,nj))
            # 주위칸이 없으면 끝
            if not l:
                continue
            growth = board[i][j] // len(l)
            for x,y in l:
                deltas.append((x,y,growth))
    for i,j,delta in deltas:
        board[i][j] += delta

def find_spot():
    l = []
    for i in range(n):
        for j in range(n):
            # 나무가 없는 칸 -> 박멸없음
            if board[i][j] <= 0:
                l.append((0,i,j))
                continue

            # 나무가 있는 칸.
            tree_cnt = board[i][j]
            for di,dj in diagnals:
                for s in range(1,k+1):
                    ni,nj = i+s*di,j+s*dj
                    # 범위 밖이거나 나무가 아니면 진행을 멈춤
                    if is_out(ni,nj) or board[ni][nj] <= 0:
                        break
                    tree_cnt += board[ni][nj]
            l.append((tree_cnt,i,j))
    l.sort(key = lambda x: (-x[0],x[1],x[2]))
    return l[0]

ans = 0
for year in range(1,m+1):
    grow_tree()
    # print("-----")
    # for row in board:
    #     print(row)
    # print("-----")
    # for row in blocked:
    #     print(row)

    tree_spread(year)
    dead_tree,ti,tj = find_spot()
    board[ti][tj] = 0
    blocked[ti][tj] = year+c
    for di,dj in diagnals:
        for s in range(1,k+1):
            ni, nj = ti+s*di,tj+s*dj
            # 범위 밖이거나 벽이면 진행을 멈춤
            if is_out(ni, nj) or board[ni][nj] == -1:
                break
            # 빈칸이면이 칸까지는 박멸
            if board[ni][nj] == 0:
                board[ni][nj] = 0
                blocked[ni][nj] = year + c
                break
            board[ni][nj] = 0
            blocked[ni][nj] = year+c

    ans += dead_tree

print(ans)
