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
    dp= [set()] ; dp[0].add((0,4,6))
    for num in numbers:
        num = int(num)
        next_candidates = set()
        min_score = 300000
        b_candidates = dp[-1]
        for b in b_candidates:
            b_score, b_left, b_right = b[0],b[1], b[2]
            if num == b_left or num == b_left: 
                if b_score + 1 < min_score:
                    next_candidates = set()
                    next_candidates.add((b_score+1,b_left,b_right))
                elif b_score + 1 == min_score:
                    next_candidates.add((b_score+1,b_left,b_right))
                min_score = b_score + 1
                continue
            
            lscore = b_score + getDist(b_left, num)
            rscore = b_score + getDist(b_right, num)
            if lscore < rscore:
                if lscore < min_score:
                    next_candidates = set()
                    next_candidates.add((lscore,num,b_right))
                elif lscore == min_score:
                    next_candidates.add((lscore,num,b_right))
                min_score = lscore
            elif lscore > rscore:
                if rscore < min_score:
                    next_candidates = set()
                    next_candidates.add((rscore,b_left,num))
                elif rscore == min_score:
                    next_candidates.add((rscore,b_left,num))
                min_score = rscore
            else:
                if lscore < min_score:
                    next_candidates = set()
                    next_candidates.add((lscore,num,b_right))
                    next_candidates.add((rscore,b_left,num))
                elif lscore == min_score:
                    next_candidates.add((lscore,num,b_right))
                    next_candidates.add((rscore,b_left,num))
                min_score = lscore
        dp.append(next_candidates)

    print(dp)
    ans = list(dp[-1])
    ans.sort(key = lambda x: x[0])
    return ans[-1][0]

print(solution("7874328"))