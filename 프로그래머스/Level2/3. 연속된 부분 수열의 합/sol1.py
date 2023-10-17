def solution(sequence, k):
    answer = []
    candidates = []

    for i in range(len(sequence)):
        sub_sum = sequence[i]
        if sub_sum == k:
            candidates.append((i,i))
        for j in range(i+1, len(sequence)):
            cur = sequence[j]
            if sub_sum + cur > k:
                break 
            elif sub_sum + cur == k:
                candidates.append((i,j))
                break
            else:
                sub_sum += cur
    min_len = 1000000000
    c2 = []
    for a,b in candidates:
        if b-a < min_len:
            min_len = b-a 
            c2.clear()
            c2.append((a,b))
        elif b-a == min_len:
            c2.append((a,b))
    
    c2.sort()
    answer.append(c2[0][0])
    answer.append(c2[0][1])
    return answer

solution([1,1,1,2,3,4,5],5)