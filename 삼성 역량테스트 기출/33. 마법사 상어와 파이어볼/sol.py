from math import floor

n,m,k = map(int,input().split())

fire_balls = [list(map(int,input().split())) for _ in range(m)]
directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
for i in range(m):
    fire_balls[i][0] -= 1
    fire_balls[i][1] -= 1
def is_all(d_list):
    odds,evens = 0,0
    for d in d_list:
        if d % 2 : odds += 1
        else: evens += 1

    return odds == 0 or evens == 0

for _ in range(k):

    board = [[[] for _ in range(n)]for _ in range(n)]
    for x,y,m,s,d in fire_balls:
        dx,dy = directions[d]
        nx,ny = (x+s*dx)%n,(y+s*dy)%n
        board[nx][ny].append((m,s,d))

    new_fire_balls = []
    for x in range(n):
        for y in range(n):
            if not board[x][y]:
                continue
            if len(board[x][y]) == 1:
                m,s,d = board[x][y][0]
                new_fire_balls.append([x,y,m,s,d])
            else:
                sum_m,sum_s,cnt = 0,0,0
                d_list = []
                for m,s,d in board[x][y]:
                    sum_m += m ; sum_s += s ; cnt += 1
                    d_list.append(d)
                new_m = floor(sum_m/5)
                new_s = floor(sum_s/cnt)
                new_d = [0,2,4,6] if is_all(d_list) else [1,3,5,7]
                if new_m == 0:
                    continue
                for d in new_d:
                    new_fire_balls.append([x,y,new_m,new_s,d])

    fire_balls = new_fire_balls

ans = 0
for (_,_,m,_,_) in fire_balls:
    ans += m
print(ans)