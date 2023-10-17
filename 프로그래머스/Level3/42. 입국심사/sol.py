def solution(n, times):
    answer = 0

    left = 1
    right = int(1e18)
    answer = right 

    while left <= right:
        mid = (left+right)//2
        people = 0
        for time in times:
            people +=  mid // time
        if people >= n :
            right = mid - 1
            answer = min(answer,mid)
        else:
            left = mid + 1
    return answer


print(solution(6, [7, 10]))