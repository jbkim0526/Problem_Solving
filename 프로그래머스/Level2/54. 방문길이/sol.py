def solution(dirs):
    answer = 0
    grid = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    l = [(-1,0),(0,1),(1,0),(0,-1)]
    d = {"U":0,"R":1,"D":2,"L":3}
    i,j = 5,5
    for s in dirs:
        dir_num = d[s]
        di,dj = l[dir_num]
        row,col = di+i,dj+j
        if 0 <= row <= 10 and 0 <= col <= 10:
            if not grid[i][j][dir_num]:
                grid[i][j][dir_num] = 1
                grid[row][col][(dir_num+2)%4] = 1
                answer += 1
            i,j = row,col
    return answer

print(solution("UUUUUUUUUUUUUUUUUUDDDDDDDDDDD"))