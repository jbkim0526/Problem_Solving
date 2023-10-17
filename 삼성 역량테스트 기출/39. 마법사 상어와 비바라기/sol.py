from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = [list(map(int,input().split())) for _ in range(m)]
board_to_cnt = [[None for _ in range(n)] for _ in range(n)]
marvels = []
directions = [(-1,0), (1, 0),(0, -1),(0, 1)]
si,sj = n//2,n//2
def initialize():
    directions = [(0, -1), (1, 0), (0, 1), (-1,0)]
    i,j,l,d,cnt = si,sj,1,0,0
    grow = False
    while True:
        for _ in range(l):
            di,dj = directions[d]
            i += di; j+= dj
            marvels.append((board[i][j]))
            board_to_cnt[i][j] = cnt
            cnt += 1
            if i ==0 and j ==0:
                return
        d = (d+1)%4
        if grow: l += 1 ;grow = False
        else: grow = True

initialize()

ans = 0
limit = len(marvels)

for d,s in moves:
    di,dj = directions[d-1]
    erase = set()
    groups = []
    for k in range(1,s+1):
        erase.add(board_to_cnt[si+k*di][sj+k*dj])
    isFirst = True
    # erase 폭발시킬 구슬들
    while erase:
        # 구슬 폭발 후 이동.
        new_marvels = []
        for i,marvel in enumerate(marvels):
            if i in erase:
                if isFirst:
                    continue
                ans += marvel
                continue
            new_marvels.append(marvel)
        marvels = new_marvels
        isFirst = False

        # 새롭게 폭발시킬 marvel
        q,groups,erase,cur_val = [],[],set(),-1
        for i,marvel in enumerate(marvels):
            if not q:
                cur_val = marvel
                q.append(i)
                continue
            if cur_val == marvel:
                q.append(i)
                continue
            # 새로운 값이 들어오면
            if len(q) >= 4:
                for elem in q:
                    erase.add(elem)
            else:
                groups.append(q)
            q = [i]
            cur_val = marvel

    new_marvels = []
    # 변화
    for group in groups:
        if len(new_marvels) > limit:
            break
        new_marvels.append(len(group))
        new_marvels.append(marvels[group[0]])
    marvels = new_marvels

print(ans)




