def solution(key, lock):

    N = len(lock)
    M = len(key)

    min_i,max_i = 20,-1
    min_j,max_j = 20,-1
    lock_points = []

    for i in range(N):
        for j in range(N):
            if lock[i][j]:
                continue 
            min_i,max_i = min(min_i,i),max(max_i,i)
            min_j,max_j = min(min_j,j),max(max_j,j)
            lock_points.append((i,j))

    target_i_len, target_j_len = max_i-min_i+1, max_j-min_j+1
    target_shape= [[1 for _ in range(target_j_len)] for _ in range(target_i_len)]
    target_points = [(i,j) for j in range(target_j_len) for i in range(target_i_len)]

    for i,j in lock_points:
        target_shape[i-min_i][j-min_j] = 0
    for k in range(4):
        if k != 0:
            key = [list(reversed(i)) for i in zip(*key)]
        
        for i in range(M-target_i_len+1):
            for j in range(M-target_j_len+1):
                for di,dj in target_points:
                    if key[i+di][j+dj] == target_shape[di][dj]:
                        break 
                else:
                    di,dj = min_i-i ,min_j-j
                    isValid = True
                    for ti in range(M):
                        if not isValid:
                            break
                        for tj in range(M):
                            ni,nj = ti+di,tj+dj
                            if 0>ni or ni>N-1 or 0>nj or nj>N-1:
                                continue
                            if lock[ni][nj] == key[ti][tj]:
                                isValid = False
                                break
                    
                    if isValid:
                        return True
    return False



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 0], [1, 1, 0], [1, 0, 1]]))