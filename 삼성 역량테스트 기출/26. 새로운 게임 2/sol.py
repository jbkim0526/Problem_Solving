import sys 
from collections import deque

input = sys.stdin.readline 

n, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

chess = [[deque() for _ in range(n)] for _ in range(n)]
locations =[]
directions = [(0,1),(0,-1),(-1,0),(1,0)]

for num in range(k):
    i,j,d = map(int,input().split())
    locations.append([(i-1,j-1),directions[d-1]])
    chess[i-1][j-1].append(num)

end = False
for turn in range(1000):
    new_locations = []
    for num,((i,j),(di,dj)) in enumerate(locations):
        ni,nj = i+di,j+dj 
        
        # 막혀있거나 파란색
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1 or board[ni][nj]== 2:
            # 반대방향으로 돌리고
            locations[num][1] = (-di,-dj)
            ni,nj = i-di,j-dj
            # 반대 방향이 막혀있거나 파란색이면 그냥 그자리에
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1 or board[ni][nj] == 2:
                continue
        n_color = board[ni][nj]
        cur_d = chess[i][j]
        next_d = chess[ni][nj]

        # 흰칸 그대로 이동
        if n_color == 0:
            temp_d = deque()
            while True:
                cur_num = cur_d.pop()
                locations[cur_num][0] = (ni,nj)
                temp_d.append(cur_num)
                if cur_num == num: break
            while len(temp_d) > 0:
                next_d.append(temp_d.pop())
 
        # 빨강 뒤집어 이동
        elif n_color == 1:
            while True:
                cur_num = cur_d.pop()
                locations[cur_num][0] = (ni,nj)
                next_d.append(cur_num)
                if cur_num == num:
                    break

        if len(next_d) >= 4:
            print(turn+1)
            end = True
            break
    if end:
        break
else:
    print(-1)

    


        




