import sys 
from math import inf
from collections import defaultdict
input = sys.stdin.readline 

N = int(input())
score = [[inf if i != j else 0 for j in range(N)] for i in range(N)]
records = [[[i+1,j+1] for j in range(N)] for i in range(N)]

for _ in range(int(input())):
    a,b,cost = map(int, input().split())
    score[a-1][b-1] = min(score[a-1][b-1],cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j :
                continue
            detour_score = score[i][k] + score[k][j]
            if score[i][j] <= detour_score:
                continue
            score[i][j] = detour_score
            records[i][j] = records[i][k] + records[k][j][1:]

for i in range(N):
    for j in range(N):
        if score[i][j] == inf:
            score[i][j] = 0

for row in score:
    print(*row)

for i in range(N):
    for j in range(N):
        if not score[i][j]:
            print(0)
            continue
        print(len(records[i][j]), *records[i][j])
    
         