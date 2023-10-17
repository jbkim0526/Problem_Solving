import sys
from collections import defaultdict, deque

n,m,k = map(int,input().split())
tower = [list(map(int,input().split())) for _ in range(n)]
attack_time = defaultdict(int)
directions = [(0,1),(1,0),(0,-1),(-1,0)]
cannon_directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
# 가장 약한 포탑 i,j return
def weakest_tower():
    tower_info = []
    for i in range(n):
        for j in range(m):
            if tower[i][j]==0:
                continue
            tower_info.append((tower[i][j],attack_time[(i,j)],i+j,j))
    tower_info.sort(key = lambda x: (x[0],-x[1],-x[2],-x[3]))
    return tower_info[0][2]-tower_info[0][3],tower_info[0][3]

def strongest_tower():
    tower_info = []
    for i in range(n):
        for j in range(m):
            if tower[i][j]==0:
                continue
            tower_info.append((tower[i][j],attack_time[(i,j)],i+j,j))
    tower_info.sort(key = lambda x: (-x[0],x[1],x[2],x[3]))
    return tower_info[0][2]-tower_info[0][3],tower_info[0][3]

# 최단경로 찾기. BFS
def laser_attack(i,j,si,sj):
    q = deque([(i,j,[])])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[i][j] = 1
    while q:
        ci,cj,path = q.popleft()
        if ci == si and cj == sj:
            return path
        for di,dj in directions:
            ni,nj = (ci+di)%n,(cj+dj)%m
            if tower[ni][nj] == 0 or visited[ni][nj]:
                continue
            new_path = path.copy()
            new_path.append((ni,nj))
            q.append((ni,nj,new_path))
            visited[ni][nj] = 1
    return None

for turn in range(1,k+1):
    fight_tower = set()
    # 약한포탑 선정
    wi,wj = weakest_tower()
    fight_tower.add((wi, wj))
    attack_time[(wi,wj)] = turn
    # 강한포탑 선정 후 공격 -> 자기자신 제외, 만약 본인이 뽑혔다면 공격대상이 없는것.
    si,sj = strongest_tower()
    if si == wi and sj == wj:
        break
    fight_tower.add((si, sj))
    tower[wi][wj] += n + m
    full_power = tower[wi][wj]
    half_power = full_power//2
    laser_path = laser_attack(wi,wj,si,sj)
    # 레이저 공격
    if laser_path:
        for i,j in laser_path[:-1]:
            fight_tower.add((i,j))
            tower[i][j] -= half_power
    # 포탄공격
    else:
        for di,dj in cannon_directions:
            ni,nj = (si+di)%n,(sj+dj)%m
            if tower[ni][nj] == 0 or ((ni==wi) and (nj==wj)):
                continue
            fight_tower.add((ni,nj))
            tower[ni][nj] -= half_power
    tower[si][sj] -= full_power

    # 포탑 부서짐 + 정비
    for i in range(n):
        for j in range(m):
            # 부서진 타워
            if tower[i][j] <= 0:
                tower[i][j] = 0
                continue
            # 부서지지 않은 포탑 중 공격과 무관하면
            if (i,j) not in fight_tower:
                tower[i][j] += 1


print(max([max(tower[i]) for i in range(n)]))