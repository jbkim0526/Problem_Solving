def solution(distance, rocks, n):
    answer = 0
    
    l,r = 0,distance+1

    rocks.sort()
    len_rocks = len(rocks)  

    while l+1 < r:
        # mid = 각 지점 사이의 거리의 최솟값
        mid = (l+r)//2
        # current = 현재 지점, count = 제거된 돌의 개수
        current = 0
        count = 0
        for i in range(len_rocks):
            # 돌이 이전 지점과 차이가 mid 이상이어야 선택가능
            if rocks[i] - current >= mid:
                current = rocks[i]
            # 돌이 이전 지점과의 차이가 mid 이하면 제거
            else:
                count += 1
        # 마지막으로 선택된 지점이 도착지점과 거리가 mid 보다 작으면 뻬야 함
        if distance - current < mid:
            count +=1
        if count > n:
            r = mid 
        else: 
            l = mid
    answer = l

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))