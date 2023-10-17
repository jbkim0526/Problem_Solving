from collections import deque

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]

dice = [[0,2,0],[4,1,3],[0,5,0],[0,6,0]]
base1  = deque([(1,0),(1,1),(1,2),(3,1)])
base2 = deque([(0,1),(1,1),(2,1),(3,1)])
left,right = base1.copy(),base1.copy()
up,down = base2.copy(),base2.copy()
left.rotate(-1) ; right.rotate(1)
up.rotate(-1); down.rotate(1)

def dice_roll(d):
    if d in [0,2]:
        temp = [dice[i][j] for i,j in (left if d==2 else right)]
        for (i,j),val in zip(base1,temp):
            dice[i][j] = val
    if d in [1,3]:
        temp = [dice[i][j] for i,j in (up if d==3 else down)]
        for (i,j),val in zip(base2,temp):
            dice[i][j] = val

def isout(i,j):
    return i < 0 or i > n-1 or j < 0 or j > m-1

ci,cj = 0,0
d = 0
ans = 0
for _ in range(k):
    di,dj = directions[d]
    ni,nj = ci+di,cj+dj
    # 이동칸 이 없음, d를 반대로
    if isout(ni,nj):
        d = (d+2)%4
        di,dj = directions[d]
        ni,nj = ci+di, cj+dj
    ci,cj = ni,nj

    # 주사위를 회전
    dice_roll(d)
    # 점수계산
    q = deque([(ci,cj)])
    b = board[ci][cj]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[ci][cj] = 1
    cnt = 1
    while q:
        i,j = q.popleft()
        for di,dj in directions:
            ni,nj = i+di,j+dj
            if isout(ni,nj) or visited[ni][nj] or board[ni][nj] != b:
                continue
            cnt += 1
            q.append((ni,nj))
            visited[ni][nj] = 1
    ans += b * cnt
    # 방향 결정
    a = dice[3][1]
    if a>b : d = (d+1)%4
    elif a<b : d = (d-1)%4

print(ans)

