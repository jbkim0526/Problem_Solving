import sys 

input = sys.stdin.readline

n,m = map(int, input().split())
i,j,face = map(int, input().split())

b = [ list(map(int, input().split())) for _ in range(n)]

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def is_clean_around(i,j):
    for di,dj in directions:
        ni,nj = i+di,j+dj 
        if ni < 0 or ni>n-1 or nj<0 or nj>m-1:
            continue 
        if not b[ni][nj]:
            return True
    return False

count = 0

while True:
    if not b[i][j]:
        b[i][j] = 2
        count += 1

    if not is_clean_around(i,j):
        new_face = (face + 2) % 4
        di,dj = directions[new_face]
        ni,nj = i+di,j+dj
        if ni < 0 or ni > n-1 or nj < 0 or nj> m-1 or b[ni][nj] == 1:
            break
        i,j = ni,nj
        continue

    face = (face-1) % 4
    di,dj = directions[face]
    ni,nj = i+di,j+dj
    if ni < 0 or ni > n-1 or nj < 0 or nj> m-1 or b[ni][nj] != 0:
        continue
    if not b[ni][nj]:
        i,j = ni,nj

print(count)