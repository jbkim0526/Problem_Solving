from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

directions = [(1,0),(0,1),(-1,0),(0,-1)]

def isout(i,j):
    return i<0 or i>n-1 or j<0 or j>n-1

# 가장 큰 블록 그룹 제거 후, 점수 return
def biggest_block_group():
    # 지정된 group을 이미 찾은 애들
    group_found = set()
    block_groups = []
    for i in range(n):
        for j in range(n):

            # 이미 group에 지정됐거나 검은 무지개 블록은 제외
            if (i,j) in group_found or board[i][j] == None or board[i][j] <= 0:
                continue
            visited = [[0 for _ in range(n)] for _ in range(n)]
            q = deque([(i,j)])
            visited[i][j] = 1
            group_found.add((i,j))
            color = board[i][j]
            block_group = [(i,j)]
            rainbow = 0
            while q:
                ci,cj = q.popleft()
                for di,dj in directions:
                    ni,nj = ci+di,cj+dj
                    # 무지개, color 색이 아니면 무시
                    if isout(ni,nj) or visited[ni][nj] or not (board[ni][nj] in [0,color]):
                        continue
                    if board[ni][nj] == 0:
                        rainbow += 1
                    else:
                        group_found.add((ni,nj))
                    visited[ni][nj] = 1
                    block_group.append((ni,nj))
                    q.append((ni,nj))
            # 2개 이하는 무시
            if len(block_group) == 1:
                continue
            block_groups.append((block_group[0][0],block_group[0][1],len(block_group),rainbow,block_group))

    if block_groups:
        block_groups.sort(key = lambda x: (-x[2],-x[3],-x[0],-x[1]))
        biggest_group = block_groups[0][-1]
        for i,j in biggest_group:
            board[i][j] = None
        return (block_groups[0][2])**2
    else:
        return -1


def rotate_45_ccw(board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[n-1-j][i] = board[i][j]
    return new_board

def gravity():
    for j in range(n):
        # 현재 column에 대해서 아래서 위로 조사
        new_column = [None]*n
        bottom = n-1

        for i in range(n-1,-1,-1):
            # -1을 발견하면 bottom 업데이트
            if board[i][j] == -1:
                new_column[i] = -1
                bottom = i-1
                continue
            # 빈칸은 무시
            if board[i][j] == None:
                continue
            # 숫자가 있으면 bottom에 쓰고 bottom을 올림
            new_column[bottom] = board[i][j]
            bottom -= 1

        for i in range(n):
            board[i][j] = new_column[i]


ans = 0
while True:
    # 가장 큰 블록 group 제거
    score = biggest_block_group()
    if score == -1:
        break
    ans += score
    # 중력, 회전, 중력
    gravity()
    board = rotate_45_ccw(board)
    gravity()
print(ans)
