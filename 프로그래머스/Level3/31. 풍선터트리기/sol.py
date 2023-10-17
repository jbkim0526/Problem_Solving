def solution(a):
    answer = 0
    n = len(a)
    left_min = [0]*n
    right_min = [0]*n

    cur_min = 1e9 
    for i in range(n):
        num = a[i]
        cur_min = min(cur_min,num)
        left_min[i] = cur_min

    cur_min = 1e9 
    for i in range(n-1,-1,-1):
        num = a[i]
        cur_min = min(cur_min,num)
        right_min[i] = cur_min 
    
    for i in range(n):
        if i == 0 or i == n-1:
            answer += 1
            continue 
        if a[i] > left_min[i-1] and a[i] > right_min[i+1]:
            continue 
        answer += 1

    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))