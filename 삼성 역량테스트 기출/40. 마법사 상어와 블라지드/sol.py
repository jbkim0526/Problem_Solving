
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
people = []
for i,j in [list(map(int,input().split())) for _ in range(m)]:
    people.append((i-1,j-1))
ei,ej = map(int,input().split())
ei -= 1 ; ej-=1
directions =[(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

def min_dist(i,j):
    return abs(ei-i)+abs(ej-j)

def is_out(i,j):
    return i<0 or i>n-1 or j<0 or j>n-1

def move():
    global people
    new_people = []
    score = 0
    for i,j in people:
        cur_dist = min_dist(i,j)
        # 최단거리가 가장 짧아지는 거로 가는게 아니라, 가능한 것 중 상하 우선인듯.
        for di,dj in directions:
            ni,nj = i+di,j+dj
            # 만약 범위 밖이거나, 가까워지지않거나, 벽이면 무시
            if is_out(ni,nj) or min_dist(ni,nj) >= cur_dist or board[ni][nj]:
                continue
            # 움직였는데 출구면 끝
            if ni == ei and nj == ej:
                score += 1
                break
            # 찾으면 바로 stop
            new_people.append((ni,nj))
            score += 1
            break
        else:
            new_people.append((i,j))
    people = new_people
    return score

def rotate(si,sj,l):
    global people
    new_board = [[0 for _ in range(l)] for _ in range(l)]
    nei,nej = -1,-1
    new_people = []
    for i in range(l):
        for j in range(l):
            if si+i == ei and sj+j == ej:
                nei = si+j ; nej = sj+l-1-i
            while (si+i,sj+j) in people:
                people.remove((si+i,sj+j))
                new_people.append((si+j,sj+l-1-i))
            new_board[j][l-1-i] = board[si+i][sj+j]
    # 회전한 것들은 내구도 감소
    for i in range(l):
        for j in range(l):
            board[si+i][sj+j] = new_board[i][j]-1 if new_board[i][j] >= 1 else 0
    # people update
    for t in new_people:
        people.append(t)

    return nei,nej

def in_rect(ri,rj,l,i,j):
    return ri <= i <= ri+l and rj <= j <= rj+l
def min_rect(i,j):
    resi, resj = -1,-1
    l = max(abs(i-ei),abs(j-ej))
    # 다 돌면서 l짜리 정사각형 그려서 확인
    for ri in range(n):
        for rj in range(n):
            if in_rect(ri,rj,l,i,j) and in_rect(ri,rj,l,ei,ej):
                return l,ri,rj
ans = 0

for t in range(k):
    # 사람들 이동
    ans += move()
    if not people:
        break
    # 정사각형 찾기
    rect_list = []
    for i,j in people:
        l,ri,rj = min_rect(i,j)
        rect_list.append((l,ri,rj))
    rect_list.sort(key = lambda x: (x[0],x[1],x[2]))
    l,ri,rj = rect_list[0]
    # 정사각형 회전, 사람도 회전해야함.
    ei,ej = rotate(ri,rj,l+1)

print(ans)
print(ei+1,ej+1)



