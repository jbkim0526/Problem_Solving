def getDist(n,m):
    d = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
    res = 0
    ni, nj = -1,-1
    mi, mj = -1,-1
    for i in range(4):
        for j in range(3):
            if d[i][j] == n: ni = i ; nj = j 
            elif d[i][j] == m: mi = i ; mj = j 
    di, dj = abs(ni-mi),abs(nj-mj)
    if di == 0 and dj == 0: 
        return 1
    while di > 0 and dj > 0: 
        di -= 1 ; dj -= 1 ; res += 3
    res += 2*di + 2*dj
    return res
        
def solution(numbers):
    answer = 0

    dp_left = [(0,4,6)]
    dp_right = [(0,4,6)]

    for num in numbers:
        num = int(num)
        before_left, before_right = dp_left[-1], dp_right[-1]
        
        l_l = before_left[0] + getDist(before_left[1], num)
        r_l = before_right[0] + getDist(before_right[1], num)
        if l_l >= r_l:
            dp_left.append((r_l,num,before_right[2]))
        else:
            dp_left.append((l_l,num,before_left[2]))
        
        l_r = before_left[0] + getDist(before_left[2], num)
        r_r = before_right[0] + getDist(before_right[2], num)
        if l_r >= r_r:
            dp_right.append((r_r,before_right[1],num))
        else:
            dp_right.append((l_r,before_left[1],num))
    answer = min(dp_left[-1][0],dp_right[-1][0])
         
    return answer