import sys
from collections import Counter
from collections import defaultdict
input = sys.stdin.readline 

x,y,ans = map(int,input().split())
r,c = 3,3

board = [list(map(int,input().split())) for _ in range(r)]

for time in range(101):

    if x-1 <= r-1 and y-1 <=c-1 and board[x-1][y-1] == ans:
        print(time)
        break
    
    if r >= c:
        total_l = []
        max_len = -1
        for i in range(r):
            count = defaultdict(int)
            for j in range(c):
                if board[i][j]:
                    count[board[i][j]] += 1
            l = []
            for k,v in count.items():
                l.append((k,v))
            l.sort(key = lambda x: (x[1],x[0]))
            max_len = max(2*len(l),max_len)
            total_l.append(l)
        new_board = [[0 for _ in range(max_len)] for _ in range(r)]
        for i,l in enumerate(total_l):
            for j,(v,cnt) in enumerate(l):
                new_board[i][2*j] = v 
                new_board[i][2*j+1] = cnt
        board = new_board
        c = max_len
        
    else:
        total_l = []
        max_len = -1
        for j in range(c):
            count = defaultdict(int)
            for i in range(r):
                if board[i][j]:
                    count[board[i][j]] += 1
            l = []
            for k,v in count.items():
                l.append((k,v))
            l.sort(key = lambda x: (x[1],x[0]))
            max_len = max(2*len(l),max_len)
            total_l.append(l)
        new_board = [[0 for _ in range(c)] for _ in range(max_len)]
        for j,l in enumerate(total_l):
            for i,(v,cnt) in enumerate(l):
                new_board[2*i][j] = v 
                new_board[2*i+1][j] = cnt
        board = new_board
        r = max_len
else:
    print(-1)




    