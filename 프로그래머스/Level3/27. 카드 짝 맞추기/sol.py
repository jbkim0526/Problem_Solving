from collections import defaultdict
from itertools import permutations
inf = 6

def ctrl_move(board,i,j,di,dj):
    while True:
        i += di ; j += dj
        if not (0<=i<=3 and 0<=j<=3):
            return i-di, j-dj
        if board[i][j] !=0:
            return i,j
        
def solution(board, r, c):
    answers = []
    d = defaultdict(list)
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    min_depths = inf 
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                continue 
            d[board[i][j]].append((i,j)) 
    
    def getMinCount(curi,curj,endi,endj,path,depths):
        global min_depths
        count = 0
        if depths >= min_depths:
            return inf
        if curi == endi and curj == endj:
            min_depths = min(min_depths,depths)
            return count
        next_coords = set()
        for di,dj in directions:
            i1,j1 = curi+di,curj+dj
            if i1<0 or i1>3 or j1<0 or j1>3:
                continue 
            if (i1,j1) not in path:
                next_coords.add((curi+di, curj+dj))
            i2,j2 = ctrl_move(board,curi,curj,di,dj)
            if (i2,j2) not in path:
                next_coords.add((i2,j2))
        if len(next_coords) == 0:
            return inf
        counts = []
        for ni,nj in next_coords:
            path.add((ni,nj))
            counts.append(getMinCount(ni,nj,endi,endj,path,depths+1) + 1) 
            path.remove((ni,nj))
        return min(counts)

    def track(order,depths,r,c):
        global min_depths
        count = 0
        if depths >= len(order):
            return count 
        i = order[depths]
        i1,j1 = d[i][0]
        i2,j2 = d[i][1]
        if i1 == r and j1 == c:
            p = set()
            p.add((i1,j1))
            min_depths = inf
            count = getMinCount(i1, j1, i2, j2, p, 0)
            board[i1][j1] = 0; board[i2][j2] = 0
            count += track(order, depths+1,i2,j2) 
            board[i1][j1] = i; board[i2][j2] = i
        elif i2 == r and j2 == c:
            p = set()
            p.add((i2,j2))
            min_depths = inf
            count = getMinCount(i2, j2, i1, j1, p, 0)
            board[i1][j1] = 0; board[i2][j2] = 0
            count += track(order, depths+1,i1,j1) 
            board[i1][j1] = i; board[i2][j2] = i
        else:
            p1,p2,p3 = set(), set(), set()
            p1.add((r,c)); p2.add((i1,j1)); p3.add((i2,j2))
            min_depths = inf
            m1 =  getMinCount(r, c, i1, j1, p1, 0)
            min_depths = inf
            m2 =  getMinCount(i1, j1, i2, j2, p2, 0)
            min_depths = inf
            m3 =  getMinCount(r, c, i2, j2, p1, 0)
            min_depths = inf
            m4 =  getMinCount(i2, j2, i1, j1, p3, 0)
            count1 = m1 + m2
            count2 = m3 + m4
            board[i1][j1] = 0; board[i2][j2] = 0
            if count1 < count2:
                count = track(order, depths+1,i2,j2) + count1
            elif count1 > count2 : 
                count = track(order, depths+1,i1,j1) + count2
            else:
                counts = []
                counts.append(track(order, depths+1,i2,j2) + count1)
                counts.append(track(order, depths+1,i1, j1) + count2)
                count = min(counts)
            board[i1][j1] = i; board[i2][j2] = i
        return count

    number_cards = len(d)
    
    if number_cards in [5,6]:
        cur_val = board[r][c] 
        if cur_val != 0:
            l = [i for i in range(1,number_cards+1)]
            l.remove(cur_val)
            orders = permutations(l)
            for order in orders:
                answers.append(track((cur_val,)+order,0,r,c))
        else:
            next_coords = set()
            for di,dj in directions:
                i1,j1 = r+di,c+dj
                if i1<0 or i1>3 or j1<0 or j1>3:
                    continue 
                if board[i1][j1] != 0:
                    next_coords.add((i1,j1,board[i1][j1]))
                i2,j2 = ctrl_move(board,r,c,di,dj)
                if board[i2][j2] != 0:
                    next_coords.add((i2,j2,board[i2][j2]))

            for i,j,card_num in next_coords:
                l = [i for i in range(1,number_cards+1)]
                l.remove(card_num)
                orders = permutations(l)
                for order in orders:
                    answers.append(track((card_num,)+order,0,i,j)+1)
    else:
        l = [i for i in range(1,number_cards+1)]
        orders = permutations(l)
        for order in orders:
            answers.append(track(order,0,r,c))

    return min(answers)+2*number_cards


print(solution([[1, 4, 4, 3], [2, 5, 5, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 2, 0))

