import sys 
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
b = [list(map(int,input().split())) for _ in range(n)]
d = {1: (0,1,2,3), 2:(0,1), 3: (0,1,2,3), 4:(0,1,2,3), 5: (0,)}
way = [(-1,0),(0,1),(1,0),(0,-1)]
cctvs = []
blind_area = n*m

for i in range(n):
    for j in range(m):
        if b[i][j] == 0:
            continue 
        blind_area -= 1
        if 0 < b[i][j] < 6:
            cctvs.append((b[i][j],i,j))


a = [d[cctv[0]] for cctv in cctvs]
c = list(product(*a))

ans = blind_area

for directions in c:
    covered_area = set()
    cur_blind_area = blind_area

    def check(i,j,way):
        count = 0
        di,dj = way
        while True:
            ni,nj = i+di,j+dj
            if ni < 0 or ni > n-1 or nj < 0 or nj> m-1 or b[ni][nj] == 6:
                break
            # cctv는 통과하나?? 
            if b[ni][nj] == 0 and (ni,nj) not in covered_area:
                covered_area.add((ni,nj))
                count += 1
            i,j = ni,nj
        return count

    for (cctv,i,j), direction in zip(cctvs,directions):
        if cctv == 1:
            cur_blind_area -= check(i,j,way[direction])
        elif cctv == 2:
            cur_blind_area -= check(i,j,way[direction])
            cur_blind_area -= check(i,j,way[(direction+2)%4])
        elif cctv == 3:
            cur_blind_area -= check(i,j,way[direction])
            cur_blind_area -= check(i,j,way[(direction+1)%4])
        elif cctv == 4:
            cur_blind_area -= check(i,j,way[(direction-1)%4])
            cur_blind_area -= check(i,j,way[direction])
            cur_blind_area -= check(i,j,way[(direction+1)%4])
        else:
            for k in range(4):
                cur_blind_area -= check(i,j,way[k])

    ans = min(ans,cur_blind_area)


print(ans)
    