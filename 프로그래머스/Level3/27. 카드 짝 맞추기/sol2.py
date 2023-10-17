from collections import defaultdict
from itertools import permutations

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
    
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                continue 
            d[board[i][j]].append((i,j)) 
    
    number_cards = len(d)
    orders = permutations([i for i in range(1,number_cards+1)])
    def getMinCount(curi,curj,endi,endj,path,depths):
        count = 0
        if depths >= 6:
            return count
        if curi == endi and curj == endj:
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
            return 10

        counts = []
        for ni,nj in next_coords:
            path.add((ni,nj))
            counts.append(getMinCount(ni,nj,endi,endj,path,depths+1) + 1) 
            path.remove((ni,nj))

        return min(counts)

    def track(order,depths,r,c):
        count = 0
        if depths >= len(order):
            return count 
        i = order[depths]
        i1,j1 = d[i][0]
        i2,j2 = d[i][1]
        p1,p2,p3 = set(), set(), set()
        p1.add((r,c)); p2.add((i1,j1)); p3.add((i2,j2))
        count1 = getMinCount(r, c, i1, j1, p1, 0) + getMinCount(i1, j1, i2, j2, p2, 0)
        count2 = getMinCount(r, c, i2, j2, p1, 0) + getMinCount(i2, j2, i1, j1, p3, 0)
        board[i1][j1] = 0; board[i2][j2] = 0
        if count1 < count2:
            count += track(order, depths+1,i2,j2) + count1
        elif count1 > count2 : 
            count += track(order, depths+1,i1,j1) + count2
        else:
            counts = []
            counts.append(track(order, depths+1,i2,j2) + count1)
            counts.append(track(order, depths+1,i1, j1) + count2)
            count = min(counts)
        board[i1][j1] = i; board[i2][j2] = i
        return count

    for order in orders:
        answers.append(track(order,0,r,c))

    return min(answers)+2*number_cards