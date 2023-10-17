from collections import deque
n,m,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
directions = [(0,1),(-1,0),(0,-1),(1,0)]
# 경로찾기
paths = []
visited = [[0 for _ in range(n)] for _ in range(n)]
teams = []
t_set = set([1,2,3])
def is_out(i,j):
    return i<0 or i>n-1 or j<0 or j>n-1
# path 찾기
def track(i, j, si, sj, path):
    if len(path) > 1 and i == si and j == sj:
        path.pop()
        paths.append(path.copy())
    for di,dj in directions:
        ni,nj = i+di,j+dj
        if is_out(ni,nj) or visited[ni][nj] or board[ni][nj]==0:
            continue
        path.append((ni, nj))
        visited[ni][nj] = 1
        track(ni,nj,si,sj,path)
for i in range(n):
    for j in range(n):
        if not board[i][j] or visited[i][j]:
            continue
        track(i,j,i,j,deque([(i,j)]))
for path in paths:
    head,tail = -1,-1
    for pi,pj in path:
        if board[pi][pj] == 1: head = (pi,pj)
        elif board[pi][pj] == 3: tail = (pi,pj)
    teams.append([head,tail])
def move_teams(teams):
    new_teams = []
    for (hi,hj),(ti,tj) in teams:
        new_head = None
        new_tail = None
        full_path = None
        # head는 4,3방향으로
        for di,dj in directions:
            ni,nj = hi+di,hj+dj
            if is_out(ni, nj) or board[ni][nj] not in [4,3]:
                continue
            if board[ni][nj] == 3:
                full_path = True
            new_head = (ni,nj)
            break
        # tail은 2방향으로
        for di,dj in directions:
            ni,nj = ti+di, tj+dj
            if is_out(ni,nj) or board[ni][nj] != 2:
                continue
            new_tail = (ni,nj)
            break
        # board, teams update
        board[new_head[0]][new_head[1]] = 1
        board[new_tail[0]][new_tail[1]] = 3
        board[hi][hj] = 2
        # 원래 tail 자리가 1이 될 수도 있음.
        board[ti][tj] = 1 if full_path else 4
        new_teams.append([new_head,new_tail])
    return new_teams
def find_wind(num):
    si,sj = -1, -1
    di,dj = -1, -1
    if num < n:
        si, sj = num, 0
        di, dj = directions[0]
    elif num < 2 * n:
        si, sj = n - 1, num-n
        di, dj = directions[1]
    elif num < 3 * n:
        si,sj = n-1-(num-2*n),n-1
        di,dj = directions[2]
    else:
        si,sj = 0, n-1-(num-3*n)
        di,dj = directions[3]
    return si,sj,di,dj
def find_count(si,sj):
    for i in range(len(paths)):
        if (si,sj) not in paths[i]:
            continue
        # 현재 팀의 머리
        hi,hj = teams[i][0]
        temp = (hi, hj)
        path = paths[i]
        head_index = path.index((hi,hj))
        next_index = (head_index+1) % len(path)
        ni,nj = path[next_index]

        d = 1 if board[ni][nj] == 2 else -1

        cnt = 1
        ci,cj = hi,hj
        while ci != si or cj != sj:
            head_index = (head_index + d) % len(path)
            ci,cj = path[head_index]
            cnt += 1

        teams[i][0] = teams[i][1]
        teams[i][1] = temp
        hi,hj = teams[i][0]
        ti,tj = teams[i][1]
        board[hi][hj] = 1
        board[ti][tj] = 3
        return cnt

ans = 0
for round in range(k):
    num = round % (4*n)
    teams = move_teams(teams)
    si,sj,di,dj = find_wind(num)
    #print(si,sj,di,dj)
    for _ in range(n):
        if board[si][sj] not in t_set:
            si += di ; sj += dj
            continue
        break
    else:
        continue
    # for row in board:
    #    print(row)
    # print(si,sj)
    res = find_count(si,sj)
    # print(res)
    ans += res**2

print(ans)


