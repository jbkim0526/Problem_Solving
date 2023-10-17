import sys 
import copy
input = sys.stdin.readline 

N = int(input())
Board = [[0 for _ in range(N)] for _ in range(N)]
count = 0

def track(board, d):
    if d >= N:
        global count
        count += 1
        return 
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                temp = copy.deepcopy(board)
                for k in range(N):
                    temp[k][j] = 1
                    temp[i][k] = 1
                for k in range(0,N):
                    if j - k < 0 or i-k < 0:
                        break
                    temp[i-k][j-k] = 1
                for k in range(0,N):
                    if j + k > N-1 or i + k > N-1:
                        break
                    temp[i+k][j+k] = 1
                for k in range(0,N):
                    if j + k > N-1 or i - k < 0:
                        break
                    temp[i-k][j+k] = 1
                for k in range(0,N):
                    if j - k < 0 or i + k > N-1:
                        break
                    temp[i+k][j-k] = 1
                track(temp,d+1)    


track(Board,0)
print(count)
    





