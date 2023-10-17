def solution(sequence):
    answer = 0
    l = [] 
    n = len(sequence)
    i = 1  

    for s in sequence:
        l.append(i*s)
        i = -i

    dp_max = [l[0]]
    dp_min = [l[0]]

    for i in range(1,n):
        cur_seq = l[i]
        dp_max.append(max(dp_max[i-1]+ cur_seq,cur_seq))
        dp_min.append(min(dp_min[i-1] + cur_seq,cur_seq))

    return max(max(dp_max),-min(dp_min))

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))