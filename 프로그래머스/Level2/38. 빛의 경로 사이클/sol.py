def getNext(i,j,k,g,m,n):

    ci = i
    cj = j
    ck = k
    cg = ''

    if g == "S":
        # up
        if k == 0:
            ck = 0
            if ci == 0:
                ci = m-1
            else:
                ci -= 1
        # down
        elif k == 1: 
            ck = 1
            if ci == m-1:
                ci = 0
            else:
                ci += 1
        # left
        elif k == 2:
            ck = 2
            if cj == 0:
                cj = n-1
            else:
                cj -= 1
        # right
        else:
            ck = 3
            if cj == n-1:
                cj = 0
            else:
                cj += 1
        

    elif g == "L":
        # up
        if k == 0:
            ck = 2
            if cj == 0:
                cj = n-1
            else:
                cj -= 1
        # down
        elif k == 1: 
            ck = 3
            if cj == n-1:
                cj = 0
            else:
                cj += 1
        # left
        elif k == 2:
            ck = 1
            if ci == m-1:
                ci = 0
            else:
                ci += 1
        # right
        else:
            ck = 0
            if ci == 0:
                ci = m-1
            else:
                ci -= 1
    else:
        # up
        if k == 0:
            ck = 3
            if cj == n-1:
                cj = 0
            else:
                cj += 1

        # down
        elif k == 1: 
            ck = 2
            if cj == 0:
                cj = n-1
            else:
                cj -= 1 


        # left
        elif k == 2:
            ck = 0
            if ci == 0:
                ci = m-1
            else:
                ci -= 1


        # right
        else:
            ck = 1
            if ci == m-1:
                ci = 0
            else:
                ci += 1



    return ci, cj, ck



def solution(grid):
    answer = []
    m = len(grid)
    n = len(grid[0])
    print(m,n)
    # up, down, left, right
    d = [[[0,0,0,0] for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(4):
                if d[i][j][k] != 0: 
                    continue 

                start = (i,j,k)
                d[i][j][k] = 1
                count = 1

                ci, cj, ck = getNext(i,j,k,grid[i][j],m,n)
                while (ci,cj,ck) != start :
                    d[ci][cj][ck] = 1 
                    count += 1
                    ci, cj, ck = getNext(ci, cj, ck, grid[ci][cj], m, n)
                answer.append(count)
                
    answer.sort()
    return answer


print(solution(["R","R"]	))