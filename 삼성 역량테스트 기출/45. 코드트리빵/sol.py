from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
temp = [list(map(int,input().split())) for _ in range(m)]
base_camps = set()
directions = [(-1,0),(0,-1),(0,1),(1,0)]
blocked = set()
goals = [(i-1,j-1) for (i,j) in temp]
for i in range(n):
    for j in range(n):
        if board[i][j]: base_camps.add((i,j))

# 현재 움지여야하는 사람 번호
moving_people = set()
# t 사람의 현재위치
people = {}

def is_out(i,j):
    return i < 0 or i>n-1 or j < 0 or j>n-1

# i,j의 사람을 최단거리 방향으로 한칸 이동 : 일단 최단경로 찾고, 그 경로에서 첫번째를 선택
def move_person(i,j,gi,gj):
    q = deque([(i,j,[])])
    visited = [[0 for _ in range(n)]for _ in range(n)]
    visited[i][j] = 1
    while q:
        ci,cj,path = q.popleft()
        if ci==gi and cj==gj:
            return path[0]

        for di,dj in directions:
            ni,nj = ci+di,cj+dj
            if is_out(ni,nj) or (ni,nj) in blocked or visited[ni][nj]:
                continue
            new_path = path[:]
            new_path.append((ni,nj))
            visited[ni][nj] = 1
            q.append((ni,nj,new_path))



# gi,gj에서 가장가까운 base camp -> DFS로 처음 발견한 거 return
def find_base_camp(gi,gj):
    q = deque([(gi, gj)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[gi][gj] = 1
    while q:
        ci,cj = q.popleft()
        if (ci,cj) in base_camps:
            base_camps.remove((ci,cj))
            return ci,cj
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if is_out(ni, nj) or (ni, nj) in blocked or visited[ni][nj]:
                continue
            visited[ni][nj] = 1
            q.append((ni, nj))

time = 0
while True:
    to_remove = set()
    # 사람들 1칸 이동
    for t in moving_people:
        i,j = people[t]
        gi,gj = goals[t]
        # 한칸 이동한 좌표
        ni,nj = move_person(i,j,gi,gj)
        # 만약 편의점에 도착했다면, 제거하기 위해 기록
        if ni == gi and nj == gj:
            to_remove.add(t)
        else:
            people[t] = (ni,nj)

    for t in to_remove:
        moving_people.remove(t)
        blocked.add(goals[t])

    # t번 사람 베이스캠프 진입.
    if time < m:
        gi,gj = goals[time]
        bi,bj = find_base_camp(gi,gj)
        blocked.add((bi, bj))
        people[time] = (bi,bj)
        moving_people.add(time)

    if not moving_people:
        break
    time += 1

print(time+1)