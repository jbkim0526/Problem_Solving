def solution(k, ranges):
    answer = []

    l = [k]
    areas = []
    
    while k > 1:
        oldk = k
        if k % 2 == 0:
            k //= 2
        else:
            k = 3*k +1
        l.append(k)
        areas.append((oldk+k)/2)

    n = len(l)
    for ra, rb in ranges:
        if ra > n + rb-1 :
            answer.append(-1)
            continue 
        else:
            answer.append(sum(areas[ra:n+rb-1]))
    return answer