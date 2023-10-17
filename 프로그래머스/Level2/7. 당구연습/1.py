def solution(m, n, startX, startY, balls):
    answer = []

    for rx,ry in balls:
        
        candidates = []
        xadd = startX + rx 
        xsub = startX - rx
        yadd = startY + ry 
        ysub = startY - ry

        if startX != rx or startY < ry:
            dy0 = xsub*xsub + yadd*yadd
            candidates.append(dy0)
        if startY != ry or startX < rx:
            dx0 = xadd*xadd + ysub*ysub
            candidates.append(dx0)
        if startX != rx or startY > ry:
            dyn = xsub*xsub + (yadd-2*n)*(yadd-2*n)
            candidates.append(dyn)
        if startY != ry or startX > rx:
            dxm = (xadd-2*m)*(xadd-2*m) + ysub*ysub
            candidates.append(dxm)
        answer.append(min(candidates))

    return answer

print(solution(10,10,3,7,[[7, 7], [2, 7], [7, 3]]))