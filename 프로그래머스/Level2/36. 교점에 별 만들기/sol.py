def solution(line):
    answer = []
    n = len(line)
    l = []
    xmax = ymax = -500
    xmin = ymin = 500
    for i in range(n):
        for j in range(i,n):
            a1,b1,c1 = line[i]
            a2,b2,c2 = line[j]
            d = b1*a2-b2*a1
            if d == 0:
                continue
            q1 = b2*c1-b1*c2
            q2 = c2*a1-c1*a2
            if q1 % d == 0 and q2 % d ==0:
                l.append((q1//d, q2//d))

    l.sort()
    xmax, xmin = l[-1][0] ,l[0][0] 
    l.sort(key = lambda x: x[1])
    ymax, ymin = l[-1][1], l[0][1]
    xr,yr = xmax-xmin+1 ,ymax-ymin+1
    
    grid = [["." for _ in range(xr)] for _ in range(yr)]

    for x,y in l:
        grid[yr-y+ymin-1][x-xmin] = "*"
    
    for row in grid:
        answer.append(''.join(row))
    return answer

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))