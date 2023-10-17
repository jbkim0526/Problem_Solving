def solution(k, ranges):
    answer = []

    l = [k]
    areas = []
    while k > 1:
        if k % 2 == 0:
            k //= 2
            l.append(k)
        else:
            k = 3*k +1
            l.append(k)

    n = len(l)
    for i in range(n-1):
        y1 = l[i]
        y2 = l[i+1]
        areas.append((y1+y2)/2)

    for ra, rb in ranges:
        if ra > n + rb-1 :
            answer.append(-1)
            continue 
        else:
            answer.append(sum(areas[ra:n+rb-1]))
    return answer

print(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]]))