import sys 
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

u = [(2,3),(2,4),(2,5),(3,6),(4,6),(5,6),(6,5),(6,4),(6,3),(5,2),(4,2),(3,2)]
d = [(8,3),(8,4),(8,5),(5,8),(4,8),(3,8),(0,5),(0,4),(0,3),(3,0),(4,0),(5,0)]
f = [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(9,5),(9,4),(9,3)]
b = [(3,8),(3,7),(3,6),(3,5),(3,4),(3,3),(3,2),(3,1),(3,0),(11,3),(11,4),(11,5)]
l = [(i,3) for i in range(12)]
r = [(11-i,5) for i in range(12)]
spin_dict = {"U":u, "D":d,"F":f,"B":b,"L":l,"R":r}
startcoord = {"U":(3,3), "D":(9,3),"F":(6,3),"B":(0,3),"L":(3,0),"R":(3,6)}
board = [['' for _ in range(9)] for _ in range(12)]

for i in range(3):
    for j in range(3,6):
        board[i][j] = "o"
for i in range(3,6):
    for j in range(9):
        if j < 3:
            board[i][j] = "g"
        elif j < 6: 
            board[i][j] = "w"
        else:
            board[i][j] = "b"
for i in range(6,9):
    for j in range(3,6):
        board[i][j] = "r"
for i in range(9,12):
    for j in range(3,6):
        board[i][j] = "y"


def rotate(board,face_id,d):
    di = 3 if d == '+' else -3
    face = spin_dict[face_id]
    vals = deque([board[i][j] for (i,j) in face])
    vals.rotate(di)
    for (i,j), val in zip(face,vals):
        board[i][j] = val
    x,y = startcoord[face_id]
    new_board = None
    if d == "-":
        new_board = [[board[x+j][y+2-i] for j in range(3)] for i in range(3)]
    else:
        new_board = [[board[x+2-j][y+i] for j in range(3)] for i in range(3)]
    
    for i in range(3):
        for j in range(3):
            board[x+i][y+j] = new_board[i][j]


def printtop(board):
    for i in range(3,6):
        s = ''
        for j in range(3,6):
            s += board[i][j]
        print(s)

t = int(input()[:-1])

for _ in range(t):
    n = int(input()[:-1])
    l = input().split()
    cur_board = deepcopy(board)
    for spin in l:
        rotate(cur_board,spin[0],spin[1])
    printtop(cur_board)