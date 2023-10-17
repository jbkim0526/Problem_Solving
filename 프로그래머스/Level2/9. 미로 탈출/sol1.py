from math import inf

def find_ij(maps):
    si = sj = li = lj = ei = ej = 0
    s = "S"
    l = "L"
    e = "E"
    for i in range(len(maps)):
        row = maps[i]
        if s in row:
            si = i
        if l in row:
            li = i
        if e in row:
            ei = i
    sj = maps[si].index(s)
    lj = maps[li].index(l)
    ej = maps[ei].index(e)
    return si,sj,li,lj,ei,ej



def solution(maps):
    answer = 0

    m = len(maps)
    n = len(maps[0])
    sx,sy,lx,ly,ex,ey = find_ij(maps)

    score = [[inf for _ in range(n)] for _ in range(m)]
    score[sx][sy] = 0 
    queue = [(sx,sy)]

    pullLever = False 
    Exit = False

    while len(queue) > 0:
        ix,iy = queue.pop(0)
        d = score[ix][iy]

        if ix == lx and iy == ly:
            # 레버에 도착.
            pullLever = True
            answer += d 
            break

        # going up
        if ix > 0 and maps[ix-1][iy] != "X":
            if score[ix-1][iy] > d + 1:
                score[ix-1][iy] = d+1
                queue.append((ix-1,iy))

        # going down
        if ix < m-1 and maps[ix+1][iy] != "X":
            if score[ix+1][iy] > d + 1:
                score[ix+1][iy] = d+1
                queue.append((ix+1,iy))
            
        # going left 
        if iy > 0 and maps[ix][iy-1] != "X":
            if score[ix][iy-1] > d + 1:
                score[ix][iy-1] = d+1
                queue.append((ix,iy-1))

        # going right
        if iy < n-1 and maps[ix][iy+1] != "X":
            if score[ix][iy+1] > d + 1:
                score[ix][iy+1] = d+1
                queue.append((ix,iy+1))

    if pullLever:
        score = [[inf for _ in range(n)] for _ in range(m)]
        score[lx][ly] = 0
        queue = [(lx,ly)]

        while len(queue) > 0:
            ix,iy = queue.pop(0)
            d = score[ix][iy]

            if ix == ex and iy == ey:
                # 끝에 도착
                Exit = True
                answer += d 
                break

            # going up
            if ix > 0 and maps[ix-1][iy] != "X":
                if score[ix-1][iy] > d + 1:
                    score[ix-1][iy] = d+1
                    queue.append((ix-1,iy))

            # going down
            if ix < m-1 and maps[ix+1][iy] != "X":
                if score[ix+1][iy] > d + 1:
                    score[ix+1][iy] = d+1
                    queue.append((ix+1,iy))
                
            # going left 
            if iy > 0 and maps[ix][iy-1] != "X":
                if score[ix][iy-1] > d + 1:
                    score[ix][iy-1] = d+1
                    queue.append((ix,iy-1))

            # going right
            if iy < n-1 and maps[ix][iy+1] != "X":
                if score[ix][iy+1] > d + 1:
                    score[ix][iy+1] = d+1
                    queue.append((ix,iy+1))
        if not Exit:
            answer = -1
    else:
        answer = -1

    return answer


print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))