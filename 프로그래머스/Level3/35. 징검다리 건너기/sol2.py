def solution(stones, k):
    left = 1
    right = int(2e8)
    answer = 0

    while left <= right:
        mid = (left+right)//2
        count = 0
        isLeft = False
        for stone in stones:
            if stone >= mid:
                count = 0
                continue 
            count += 1
            if count >= k:
                isLeft = True 
                break
        if isLeft:
            right = mid-1 
        else:
            answer = max(answer,mid)
            left = mid + 1
           
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))