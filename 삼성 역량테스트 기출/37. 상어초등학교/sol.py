from collections import defaultdict

n = int(input())
num_student = n**2
likes = [list(map(int,input().split())) for _ in range(num_student)]
adjancents = defaultdict(list)
board = [[0 for _ in range(n)] for _ in range(n)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
likes_dict = dict()
def isout(i,j):
    return i < 0 or i>n-1 or j<0 or j>n-1

def adjacent_blank(i,j):
    cnt = 0
    for di,dj in directions:
        ni,nj=i+di,j+dj
        if isout(ni,nj) or board[ni][nj]:
            continue
        cnt += 1
    return cnt

for s0,s1,s2,s3,s4 in likes:
    total = defaultdict(int)
    likes_dict[s0] = [s1,s2,s3,s4]
    for s in [s1,s2,s3,s4]:
        # s1,s2,s3,s4가 인접한 칸들을 조사
        for (i,j) in adjancents[s]:
            if board[i][j]:
                continue
            total[(i,j)] += 1
    l = []
    ti,tj = -1,-1
    for (i,j),v in total.items():
        l.append((i,j,v,adjacent_blank(i,j)))
    # l이 있으면 정렬해서 첫번째 i,j
    if l:
        l.sort(key = lambda x : (-x[2],-x[3],x[0],x[1]))
        ti,tj,_,_ = l[0]
    # 없으면 2중 for문으로, 처음 max_blank를 달성하는 i,j
    else:
        max_blank = -1
        for i in range(n):
            for j in range(n):
                if board[i][j]:
                    continue
                # 빈칸에 대해, 주위 빈칸 개수 count
                cur_blank = adjacent_blank(i,j)
                if cur_blank > max_blank:
                    max_blank = cur_blank
                    ti,tj = i,j
    board[ti][tj] = s0
    like_cnt = 0
    for di,dj in directions:
        ni,nj = ti+di,tj+dj
        if isout(ni,nj):
            continue
        adjancents[s0].append((ni,nj))


# 자리배치 끝
ans = 0
scores = {0:0,1:1,2:10,3:100,4:1000}
for i in range(n):
    for j in range(n):
        cnt = 0
        like = likes_dict[board[i][j]]
        for di,dj in directions:
            ni,nj = i+di,j+dj
            if isout(ni,nj) or (not board[ni][nj] in like):
                continue
            cnt += 1
        ans += scores[cnt]

print(ans)

