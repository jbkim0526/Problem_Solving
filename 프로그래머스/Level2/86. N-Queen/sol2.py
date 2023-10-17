from copy import deepcopy
d = [(1,1),(1,0),(1,-1)]

def track(grid, count, n, available):
    num = 0
    if count > n:
        return num+1
    
    i = count -1
    if n % 2 == 0 and i == 0:
        nj = n // 2
        for j in range(nj):
            if grid[i][j] != -1:
                temp = deepcopy(grid)
                navailable = available
                for di,dj in d:
                    si,sj = i,j
                    while 0<=si<=n-1 and 0<=sj<=n-1:
                        if temp[si][sj] != -1: 
                            navailable -= 1
                            temp[si][sj] = -1 
                        si+=di ; sj+=dj
                if n-count <= navailable:
                    num += track(temp,count+1,n,navailable)
                print(j, num)
        num *= 2
        
    else:
        for j in range(n):
            if grid[i][j] != -1:
                temp = deepcopy(grid)
                navailable = available
                for di,dj in d:
                    si,sj = i,j
                    while 0<=si<=n-1 and 0<=sj<=n-1:
                        if temp[si][sj] != -1: 
                            navailable -= 1
                            temp[si][sj] = -1 
                        si+=di ; sj+=dj
                if n-count <= navailable:
                    num += track(temp,count+1,n,navailable)
    return num

def solution(n):
    answer = 0
    grid = [[0 for  _ in range(n)] for _ in range(n)]
    answer = track(grid,1,n, n**2)
    return answer

print(solution(12))