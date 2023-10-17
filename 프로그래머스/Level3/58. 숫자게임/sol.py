def solution(A, B):
    answer = 0
    A.sort(reverse= True)
    B.sort(reverse= True)
    for num in A:
        left,right = -1,len(B)
        while left+1 < right:
            mid = (left+right)//2
            if B[mid] <= num:
                right = mid
            else:
                left = mid
        if left < 0:
            B.pop()
            continue
        B.remove(B[left])
        answer += 1
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))